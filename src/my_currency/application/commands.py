"""
Commands module.

This module contains all available commands (let's called use cases) for the application.
"""

from dataclasses import dataclass
from datetime import datetime

from my_currency.dependency_injection.dispatcher import ICommand


@dataclass(frozen=True)
class GetCurrencyRatesByPeriodCommand(ICommand):
    """GetCurrencyRatesByPeriod command."""

    source_currency: str
    date_from: str
    date_to: str


@dataclass(frozen=True)
class GetExchangeRateDataCommand(ICommand):
    """GetExchangeRateData Command."""

    source_currency: str
    exchanged_currency: str
    valuation_date: datetime
    provider: str
