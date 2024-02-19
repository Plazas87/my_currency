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
        currencies = [obj.source_currency, obj.exchange_currency]
        saved_currencies = []

        for currency in currencies:
            saved_currency, _ = Currency.objects.update_or_create(
                id=currency.id,
                defaults={
                    "symbol": currency.symbol,
                    "name": currency.name,
                    "code": currency.code,
                    "id": currency.id,
                },
            )
            saved_currencies.append(saved_currency)

        CurrencyExchangeRate.objects.update_or_create(
            source_currency=obj.source_currency.id,
            exchange_currency=obj.exchange_currency.id,
            valuation_date=obj.valuation_date,
            defaults={
                "id": obj.id,
                "source_currency": saved_currencies[0],
                "exchange_currency": saved_currencies[1],
                "valuation_date": obj.valuation_date,
                "rate_value": obj.rate_value,
            },
        )

    def save_bulk(self, objs: List[CurrencyExchangeRateDTO]) -> None:
        """Save many instacnces at once."""
        for obj in objs:
            self.save(obj=obj)

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
