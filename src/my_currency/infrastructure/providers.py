"""Providers implementation module."""

import logging
import random
from datetime import datetime
from typing import Any, Dict, List, Optional, Type

from asgiref.sync import async_to_sync

from my_currency.application.dtos import ProviderDTO, ProviderPriority
from my_currency.application.interfaces import (
    IExecutor,
    IProvider,
    IProviderManager,
    IProvidersFinder,
)
from my_currency.application.requests import HTTPRequest
from my_currency.application.responses import ExchangeRatesResponse, HTTPResponse

logger = logging.getLogger(__name__)


class ProviderManager(
    IProviderManager[IProvider[str, ExchangeRatesResponse, ProviderPriority]]
):
    """
    ProviderManager class.

    This class manage all the operations related to providers.
    """

    _providers: Dict[str, Type[IProvider[str, ExchangeRatesResponse, ProviderPriority]]]
    _request_executor: IExecutor[HTTPRequest, HTTPResponse]
    _provider_finder: IProvidersFinder[str, ProviderDTO]
    _available_symbols: List[str]

    def __init__(
        self,
        providers: Dict[
            str, Type[IProvider[str, ExchangeRatesResponse, ProviderPriority]]
        ],
        request_executor: IExecutor[HTTPRequest, HTTPResponse],
        provider_finder: IProvidersFinder[str, ProviderDTO],
        available_symbols: List[str],
    ) -> None:
        """Class constructor."""
        self._providers = providers
        self._request_executor = request_executor
        self._provider_finder = provider_finder
        self._available_symbols = available_symbols

    def get_providers(
        self,
    ) -> List[IProvider[str, ExchangeRatesResponse, ProviderPriority]]:
        """Return a list of available providers ordered by priority."""
        providers: List[IProvider] = []

        for provider_name, provider_cls in self._providers.items():
            provider = self._provider_finder.get_by_name(name=provider_name)
            if provider is None:
                continue

            providers.append(
                provider_cls(
                    request_executor=self._request_executor,
                    name=provider.name,
                    priority=provider.priority,
                    method=provider.method,
                    url=provider.url,
                    access_key=provider.access_key,
                    available_symbols=self._available_symbols,
                )
            )

        return sorted(providers, key=lambda provider: provider.priority)


class FixerProvider(IProvider[str, ExchangeRatesResponse, ProviderPriority]):
    """Fixer.io Provider implementation."""

    _request_executor: IExecutor[HTTPRequest, HTTPResponse]
    _name: str
    _priority: ProviderPriority
    _method: str
    _url: str
    _access_key: str
    _available_symbols: List[str]

    def __init__(
        self,
        request_executor: IExecutor[HTTPRequest, HTTPResponse],
        name: str,
        priority: ProviderPriority,
        method: str,
        url: str,
        access_key: str,
        available_symbols: List[str],
    ) -> None:
        """Class constructor."""
        self._request_executor = request_executor
        self._name = name
        self._priority = priority
        self._method = method
        self._url = url
        self._access_key = access_key
        self._available_symbols = available_symbols

    @property
    def priority(self) -> ProviderPriority:
        """Return the provider priority."""
        return self._priority

    def get_currencies(
        self,
        source_currency: str,
        valuation_date: str,
        exchange_courrency: Optional[str] = None,
    ) -> List[ExchangeRatesResponse]:
        """Get latest currencies."""
        rates: List[ExchangeRatesResponse] = []

        request = self._build_request(
            source_currency=source_currency,
            valuation_date=valuation_date,
            exchange_courrency=exchange_courrency,
        )

        sync_executor = async_to_sync(self._request_executor.execute)
        request_response = sync_executor(request)

        if 200 <= request_response.status_code < 300:
            return self._response_to_exchange_rates_response(
                source_currency=source_currency, response=request_response.body
            )

        return rates

    def _response_to_exchange_rates_response(
        self, source_currency: str, response: Dict[str, Any]
    ) -> List[ExchangeRatesResponse]:
        """Transform the http response data to a ExchangeRatesResponse object."""
        rates: List[ExchangeRatesResponse] = []

        for exchange_currency, rate_value in response["rates"].items():

            try:
                rates.append(
                    ExchangeRatesResponse(
                        source_currency=source_currency,
                        exchange_currency=exchange_currency,
                        valuation_date=datetime.strptime(response["date"], "%Y-%m-%d"),
                        rate_value=rate_value,
                    )
                )

            except Exception as error:
                logger.warning(
                    "Provider malformed response. The provider may have change the response interface: '%s'",
                    str(error),
                )
                logger.debug("Provider response: %s", response)
                break

        return rates

    def _build_request(
        self,
        source_currency: str,
        valuation_date: str,
        exchange_courrency: Optional[str],
    ) -> HTTPRequest:
        return HTTPRequest(
            method=self._method,
            url=self._build_url(endpoint_path=valuation_date),
            query_params=self._build_query_params(
                source_currency=source_currency, exchange_courrency=exchange_courrency
            ),
        )

    def _build_url(self, endpoint_path: str) -> str:
        return self._url + endpoint_path

    def _build_query_params(
        self, source_currency: str, exchange_courrency: Optional[str]
    ) -> Dict[str, Any]:
        query_params = {
            "access_key": self._access_key,
            "base": source_currency,
            "symbols": ", ".join(
                [
                    symbol
                    for symbol in self._available_symbols
                    if symbol != source_currency
                ]
            ),
        }
        if exchange_courrency is not None:
            query_params.update({"symbols": exchange_courrency})

        return query_params


class MockProvider(IProvider[str, ExchangeRatesResponse, ProviderPriority]):
    """Mock Provider implementation."""

    _request_executor: IExecutor[HTTPRequest, HTTPResponse]
    _name: str
    _priority: ProviderPriority
    _method: str
    _url: str
    _access_key: str
    _available_symbols: List[str]

    def __init__(
        self,
        request_executor: IExecutor[HTTPRequest, HTTPResponse],
        name: str,
        priority: ProviderPriority,
        method: str,
        url: str,
        access_key: str,
        available_symbols: List[str],
    ) -> None:
        """Class constructor."""
        self._request_executor = request_executor
        self._name = name
        self._priority = priority
        self._method = method
        self._url = url
        self._access_key = access_key
        self._available_symbols = available_symbols

    @property
    def priority(self) -> ProviderPriority:
        """Return the provider priority."""
        return self._priority

    def get_currencies(
        self,
        source_currency: str,
        valuation_date: str,
        exchange_courrency: Optional[str] = None,
    ) -> List[ExchangeRatesResponse]:
        """Get latest currencies."""
        rates: List[ExchangeRatesResponse] = []

        # Generate random rates
        rates = [
            self._generate_random_rate(
                exchange_currency=symbol, valuation_date=valuation_date
            )
            for symbol in self._available_symbols
        ]

        return rates

    def _generate_random_rate(
        self, exchange_currency: str, valuation_date: str
    ) -> ExchangeRatesResponse:
        source_currency = "EUR"  # Assuming source currency is always EUR
        rate_value = random.uniform(0.5, 1.5)

        return ExchangeRatesResponse(
            source_currency=source_currency,
            exchange_currency=exchange_currency,
            valuation_date=valuation_date,
            rate_value=rate_value,
        )
