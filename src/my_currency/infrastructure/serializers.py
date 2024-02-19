"""Serializers module."""
import uuid

from my_currency.application.dtos import CurrencyDTO, CurrencyExchangeRateDTO
from my_currency.application.interfaces import ISerializer
from my_currency.application.responses import ExchangeRatesResponse
from my_currency.application.symbols import currency_code_name_map


class ExchangeRatesResponseSerializer(
    ISerializer[ExchangeRatesResponse, CurrencyExchangeRateDTO]
):
    """ExchangeRatesResponse Serializer."""

    def serialize(self, obj: ExchangeRatesResponse) -> CurrencyExchangeRateDTO:
        """Transform a ExchangeRatesResponse to a CurrencyExchangeRateDTO."""
        return CurrencyExchangeRateDTO(
            id=uuid.uuid4(),
            source_currency=CurrencyDTO(
                id=uuid.uuid4(),
                code=obj.source_currency,
                name=currency_code_name_map[obj.source_currency],
                symbol=obj.source_currency,
            ),
            exchange_currency=CurrencyDTO(
                id=uuid.uuid4(),
                code=obj.exchange_currency,
                name=currency_code_name_map[obj.exchange_currency],
                symbol=obj.exchange_currency,
            ),
            valuation_date=obj.valuation_date,
            rate_value=obj.rate_value,
        )
