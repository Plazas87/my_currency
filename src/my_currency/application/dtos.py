"""Data transfer objests module."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class ProviderDTO:
    """Provider data trasnfer object."""

    id: str
    name: str
    priority: str
    method: str
    url: str
    access_key: str


@dataclass
class ProviderPriority:
    """Provider priority."""

    value: int
    name: str


@dataclass(frozen=True)
class CurrencyDTO:
    """Currency data transfer object."""

    id: str
    code: str
    name: str
    symbol: str


@dataclass(frozen=True)
class CurrencyExchangeRateDTO:
    """CurrencyExchangeRate data transfer object."""

    id: str
    source_currency: CurrencyDTO
    exchange_currency: CurrencyDTO
    valuation_date: str
    rate_value: Decimal
