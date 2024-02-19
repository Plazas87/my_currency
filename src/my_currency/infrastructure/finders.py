"""Finders module."""

from datetime import datetime
from typing import List, Optional

from my_currency.application.dtos import (
    CurrencyDTO,
    CurrencyExchangeRateDTO,
    ProviderDTO,
)
from my_currency.application.interfaces import (
    ICurrencyFinder,
    IExchangeCurrenteRateFinder,
    IProvidersFinder,
)
from my_currency.controllers.apps.currencies.models import (
    Currency,
    CurrencyExchangeRate,
)
from my_currency.controllers.apps.providers.models import Provider


class CurrencyFinder(ICurrencyFinder[str, CurrencyDTO]):
    """Curency finder imiplementation."""

    def get_by_code(self, code: str) -> CurrencyDTO | None:
        """Get Currencies by code."""
        try:
            currency = Currency.objects.get(code=code)

        except Currency.DoesNotExist:
            return None

        return CurrencyDTO(
            id=currency.id,
            code=currency.code,
            name=currency.name,
            symbol=currency.symbol,
        )


class CurrencyExchangeRateFinder(
    IExchangeCurrenteRateFinder[str, CurrencyExchangeRateDTO]
):
    """CurrencyExchangeRate Finder."""

    def get_by_source_currency_and_date_period(
        self, source_currency: str, date_from: str, date_to: str
    ) -> List[CurrencyExchangeRateDTO]:
        """Get all available obj by ID."""
        start_date = datetime.strptime(date_from, "%Y-%m-%d")
        end_date = datetime.strptime(date_to, "%Y-%m-%d")
        exchange_rates_queryset = CurrencyExchangeRate.objects.filter(
            source_currency__code=source_currency,
            valuation_date__range=(start_date, end_date),
        )

        return [
            self._to_currency_exchange_rate_dto(exchange_rate)
            for exchange_rate in exchange_rates_queryset
        ]

    def _to_currency_exchange_rate_dto(
        self, exchange_currency_rate: CurrencyExchangeRate
    ) -> CurrencyExchangeRateDTO:
        """Build a ExcahngeCurrencyRateDTO instance."""
        return CurrencyExchangeRateDTO(
            id=str(exchange_currency_rate.id),
            source_currency=self._to_currency_dto(
                currency=exchange_currency_rate.source_currency
            ),
            exchange_currency=self._to_currency_dto(
                currency=exchange_currency_rate.exchange_currency
            ),
            valuation_date=exchange_currency_rate.valuation_date,
            rate_value=exchange_currency_rate.rate_value,
        )

    def _to_currency_dto(self, currency: Currency) -> CurrencyDTO:
        """Build a ExchangeCurrencyDTO."""
        return CurrencyDTO(
            id=str(currency.id),
            code=currency.code,
            name=currency.name,
            symbol=currency.symbol,
        )


class ProvidersFinder(IProvidersFinder[str, ProviderDTO]):
    """Providers Finder."""

    def get_by_name(self, name: str) -> Optional[ProviderDTO]:
        """Get all available obj by name and owner ID."""
        try:
            provider = Provider.objects.get(name=name)

        except Exception:
            return None

        return self._to_provider_dto(provider=provider)

    def _to_provider_dto(self, provider: Provider) -> ProviderDTO:
        """Build a provider dto instace."""
        return ProviderDTO(
            id=str(provider.id),
            name=provider.name,
            priority=provider.priority,
            method=provider.method,
            url=provider.url,
            access_key=provider.access_key,
        )
