"""Repositories module."""

import uuid
from dataclasses import asdict
from typing import List
from uuid import UUID

from my_currency.application.dtos import CurrencyDTO, CurrencyExchangeRateDTO
from my_currency.application.interfaces import IRepository
from my_currency.controllers.apps.currencies.models import (
    Currency,
    CurrencyExchangeRate,
)


class CurrencyExchangeRateRepository(IRepository[CurrencyExchangeRateDTO, UUID, None]):
    """CurrencyExchangeRate repository class."""

    @staticmethod
    def generate_uuid() -> UUID:
        """Generate an uuid."""
        return uuid.uuid4()

    def save(self, obj: CurrencyExchangeRateDTO) -> None:
        """Save an obj in the database."""
        raise NotImplementedError

    def save_bulk(self, objs: List[CurrencyExchangeRateDTO]) -> None:
        """Save many instacnces at once."""
        currencies_to_save = []
        exchange_currency_rates_to_save = []

        source_currency_to_save = self._create_currency_from_currency_dto(
            currency_dto=objs[0].source_currency
        )
        currencies_to_save.append(source_currency_to_save)

        for currency_exchange_rate in objs:
            exchange_currency_to_save = self._create_currency_from_currency_dto(
                currency_dto=currency_exchange_rate.exchange_currency
            )
            currencies_to_save.append(exchange_currency_to_save)

            exchange_currency_rates_to_save.append(
                CurrencyExchangeRate(
                    id=currency_exchange_rate.id,
                    source_currency=source_currency_to_save,
                    exchange_currency=exchange_currency_to_save,
                    valuation_date=currency_exchange_rate.valuation_date,
                    rate_value=currency_exchange_rate.rate_value,
                )
            )

        Currency.objects.bulk_create(currencies_to_save)
        CurrencyExchangeRate.objects.bulk_create(exchange_currency_rates_to_save)

    def _create_currency_from_currency_dto(self, currency_dto: CurrencyDTO) -> Currency:
        courrency_as_dict = asdict(currency_dto)
        return Currency(**courrency_as_dict)

    def update(self, obj: CurrencyExchangeRateDTO) -> None:
        """Update an obj in the database."""
        raise NotImplementedError


class ProviderRepository(IRepository[CurrencyExchangeRateDTO, UUID, None]):
    """Provider repository class."""

    @staticmethod
    def generate_uuid() -> UUID:
        """Generate an uuid."""

    def save(self, obj: CurrencyExchangeRateDTO) -> None:
        """Save an obj in the database."""
        pass

    def update(self, obj: CurrencyExchangeRateDTO) -> None:
        """Update an obj in the database."""
        pass

    def remove(self, obj: CurrencyExchangeRateDTO) -> None:
        """Remove a Provider from the available providers list."""
