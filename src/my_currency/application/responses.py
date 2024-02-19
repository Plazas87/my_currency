"""Application data transfer object module."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Dict


@dataclass(frozen=True)
class HTTPResponse:
    """ExecutionResponse data transfer object."""

    status_code: bool
    headers: Dict[str, str]
    body: Dict[str, Any]


@dataclass(frozen=True)
class ExchangeRatesResponse:
    """Exchange Rates Response."""

    source_currency: str
    exchange_currency: str
    valuation_date: str
    rate_value: Decimal
