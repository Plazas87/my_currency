"""
Comand handlers module.

This module contain all the handlers for all available use cases in the application.
"""

import logging
from typing import Callable, List
from uuid import UUID

from my_currency.application.commands import GetCurrencyRatesByPeriodCommand
from my_currency.application.dtos import CurrencyDTO, CurrencyExchangeRateDTO
from my_currency.application.interfaces import (
    ICurrencyFinder,
    IExchangeCurrenteRateFinder,
    IExecutor,
    IProvider,
    IProviderManager,
    IRepository,
    ISerializer,
    ITimeSeriesGenerator,
)
from my_currency.application.requests import HTTPRequest
from my_currency.application.responses import ExchangeRatesResponse, HTTPResponse
from my_currency.application.symbols import currency_code_name_map
from my_currency.dependency_injection.dispatcher import IHandler

logger = logging.getLogger(__name__)


class GetCurrencyRatesByPeriodCommandHandler(
    IHandler
):  # pylint: disable=too-few-public-methods
    """GetCurrencyRatesByPeriodCommand Handler."""

    _executor: IExecutor[HTTPRequest, HTTPResponse]
    _provider_manager: IProviderManager[IProvider]
    _exchange_rates_repository: IRepository[CurrencyExchangeRateDTO, UUID, None]
    _exchange_rates_finder: IExchangeCurrenteRateFinder[str, CurrencyExchangeRateDTO]
    _currency_finder: ICurrencyFinder[str, CurrencyDTO]
    _get_exchange_rate_data: Callable[[str, str, IProvider, str], HTTPResponse]
    _available_currency_symbols: List[str]
    _days_between_generator: ITimeSeriesGenerator
    _exchange_rates_response_serializer: ISerializer[
        ExchangeRatesResponse, CurrencyExchangeRateDTO
    ]

    def __init__(
        self,
        executor: IExecutor[HTTPRequest, HTTPResponse],
        provider_manager: IProviderManager,
        exchange_rates_repository: IRepository[CurrencyExchangeRateDTO, UUID, None],
        exchange_rates_finder: IExchangeCurrenteRateFinder[
            str, CurrencyExchangeRateDTO
        ],
        currency_finder: ICurrencyFinder[str, CurrencyDTO],
        get_exchange_rate_data: Callable[[str, str, IProvider, str], HTTPResponse],
        available_currency_symbols: List[str],
        days_between_generator: ITimeSeriesGenerator[str],
        exchange_rates_response_serializer: ISerializer[
            ExchangeRatesResponse, CurrencyExchangeRateDTO
        ],
    ) -> None:
        """Class constructor."""
        self._executor = executor
        self._provider_manager = provider_manager
        self._exchange_rates_repository = exchange_rates_repository
        self._exchange_rates_finder = exchange_rates_finder
        self._currency_finder = currency_finder
        self._get_exchange_rate_data = get_exchange_rate_data  # type: ignore
        self._available_currency_symbols = available_currency_symbols
        self._days_between_generator = days_between_generator
        self._exchange_rates_response_serializer = exchange_rates_response_serializer

    def handle(
        self, command: GetCurrencyRatesByPeriodCommand
    ) -> List[ExchangeRatesResponse]:
        """Handle a train command."""
        logger.info("Start Handling '%s'", command)
        exchange_rates: List[ExchangeRatesResponse] = []
        dates = self._days_between_generator.generate(
            start_date=command.date_from, end_date=command.date_to
        )
        exchange_rates = self._to_exchange_rate_response(
            currency_exchange_rate_dtos=self._exchange_rates_finder.get_by_source_currency_and_date_period(
                source_currency=command.source_currency,
                date_from=command.date_from,
                date_to=command.date_to,
            )
        )

        if not exchange_rates:
            providers: List[IProvider] = self._provider_manager.get_providers()

            for provider in providers:
                try:
                    exchange_rates = (
                        self._get_available_currencies_from_external_source(
                            command=command, dates=dates, provider=provider
                        )
                    )
                    if exchange_rates:
                        break

                except Exception as error:
                    logger.warning(
                        "Error while trying to fetch rates from provider '%s': %s",
                        provider.__class__.__name__,
                        error,
                    )
                    continue

            if currency_exchange_rate_dtos := self._to_currency_exchange_rate_dtos(
                exchange_rates_responses=exchange_rates,
                source_currency=command.source_currency,
            ):
                self._exchange_rates_repository.save_bulk(
                    objs=currency_exchange_rate_dtos
                )

        logger.info("Command '%s' successfully executed.", command)

        return exchange_rates

    def _to_exchange_rate_response(
        self, currency_exchange_rate_dtos: List[CurrencyExchangeRateDTO]
    ) -> List[ExchangeRatesResponse]:
        exchange_rate_responses = []
        for currency_exchange_rate_dto in currency_exchange_rate_dtos:
            exchange_rate_responses.append(
                ExchangeRatesResponse(
                    source_currency=currency_exchange_rate_dto.source_currency.code,
                    exchange_currency=currency_exchange_rate_dto.exchange_currency.code,
                    valuation_date=currency_exchange_rate_dto.valuation_date,
                    rate_value=currency_exchange_rate_dto.rate_value,
                )
            )

        return exchange_rate_responses

    def _get_available_currencies_from_external_source(
        self,
        provider: IProvider,
        dates: List[str],
        command: GetCurrencyRatesByPeriodCommand,
    ):
        """Fetch the lastes currencies for available simbols by a period."""
        rates: List[ExchangeRatesResponse] = []
        for date in dates:
            exchange_rates: List[ExchangeRatesResponse] = self._get_exchange_rate_data(  # type: ignore
                source_currency=command.source_currency,
                valuation_date=date,
                provider=provider,
            )

            if exchange_rates:
                rates.extend(exchange_rates)

        return rates

    def _to_currency_exchange_rate_dtos(
        self,
        exchange_rates_responses: List[ExchangeRatesResponse],
        source_currency: str,
    ) -> List[CurrencyExchangeRateDTO]:
        currency_exchange_rates: List[CurrencyExchangeRateDTO] = []
        source_currency_dto = self._get_or_create_currency_dto(source_currency)

        for exchange_rates_response in exchange_rates_responses:
            exchange_currency = self._get_or_create_currency_dto(
                exchange_rates_response.exchange_currency
            )

            currency_exchange_rates.append(
                CurrencyExchangeRateDTO(
                    id=str(self._exchange_rates_repository.generate_uuid()),
                    source_currency=source_currency_dto,
                    exchange_currency=exchange_currency,
                    valuation_date=exchange_rates_response.valuation_date,
                    rate_value=exchange_rates_response.rate_value,
                )
            )

        return currency_exchange_rates

    def _get_or_create_currency_dto(self, currency_code: str) -> CurrencyDTO:
        currency_dto = self._currency_finder.get_by_code(code=currency_code)

        if currency_dto is None:
            currency_dto = CurrencyDTO(
                id=str(self._exchange_rates_repository.generate_uuid()),
                code=currency_code,
                name=currency_code_name_map[currency_code],
                symbol=currency_code,
            )

        return currency_dto
