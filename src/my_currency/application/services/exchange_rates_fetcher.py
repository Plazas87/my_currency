"""Application services."""

from typing import List, Optional

from my_currency.application.interfaces import IProvider
from my_currency.application.responses import ExchangeRatesResponse


def get_exchange_rate_data(
    source_currency: str,
    valuation_date: str,
    provider: IProvider,
    exchange_courrency: Optional[str] = None,
) -> List[ExchangeRatesResponse]:
    """Retrive data from a third party provider."""
    if exchange_courrency is not None:
        return provider.get_currencies(
            source_currency=source_currency,
            valuation_date=valuation_date,
            exchange_courrency=exchange_courrency,
        )

    return provider.get_currencies(
        source_currency=source_currency, valuation_date=valuation_date
    )
