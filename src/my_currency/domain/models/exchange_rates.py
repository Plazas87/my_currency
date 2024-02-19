"""Exchange Rates models module."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from .exceptions import (
    CurrencyCodeLenghtValidationError,
    CurrencyExchangeRateEvaluationDateError,
    CurrencyExchangeRateExchangeCurrencyError,
    CurrencyExchangeRateIdError,
    CurrencyExchangeRateRateValueError,
    CurrencyExchangeRateSourceCurrencyError,
    CurrencyIdValidationError,
    CurrencyNameLenghtValidationError,
    CurrencySymbolLenghtValidationError,
)


@dataclass(frozen=True)
class CurrencyExchangeRateId:
    """CurrencyExchangeRate ID value object."""

    value: UUID

    def __post_init__(self) -> None:
        """Post init validations."""
        if not isinstance(self.value, UUID):
            raise CurrencyExchangeRateIdError(
                message="Invalid UUID. It should be a UUID instance."
            )

    @classmethod
    def from_string(cls, value: str) -> CurrencyExchangeRateId:
        """Create a CurrencyId instance from a uuid string."""
        try:

            uuid = UUID(value)

        except ValueError as error:
            raise CurrencyIdValidationError(
                message=f"Invalid string uuid: {value}"
            ) from error

        return cls(value=uuid)


@dataclass(frozen=True)
class CurrencyExchangeRateSourceCurrency:
    """CurrencyExchangeRateSourceCurrency value object."""

    value: str

    def __post_init__(self) -> None:
        """Post init validations."""
        if isinstance(self.value, Currency):
            raise CurrencyExchangeRateSourceCurrencyError(
                message="Invalid Source Currency. It sould be a 'Currency' instance."
            )


@dataclass(frozen=True)
class CurrencyExchangeRateExchangeCurrency:
    """CurrencyExchangeRateExchangeCurrency value object."""

    value: str

    def __post_init__(self) -> None:
        """Post init validations."""
        if isinstance(self.value, Currency):
            raise CurrencyExchangeRateExchangeCurrencyError(
                message="Invalid Exchange currency. It sould be a 'Currency' instance."
            )


@dataclass(frozen=True)
class CurrencyExchangeRateEvaluationDate:
    """CurrencyExchangeRateEvaluationDate value object."""

    value: str

    def __post_init__(self) -> None:
        """Post init validations."""
        if isinstance(self.value, datetime):
            raise CurrencyExchangeRateEvaluationDateError(
                message="Invalid Evaluation date. It sould be a 'datetime' instance."
            )


@dataclass(frozen=True)
class CurrencyExchangeRateRateValue:
    """CurrencyExchangeRateRateValue value object."""

    value: Decimal

    def __post_init__(self) -> None:
        """Post init validations."""
        if isinstance(self.value, Decimal):
            raise CurrencyExchangeRateRateValueError(
                message="Invalid Evaluation date. It sould be a 'Decimal' instance."
            )


class CurrencyExchangeRate:
    """Currency exchange rate model."""

    id: CurrencyExchangeRateId
    source_currency: CurrencyExchangeRateSourceCurrency
    exchange_currency: CurrencyExchangeRateExchangeCurrency
    valuation_date: CurrencyExchangeRateEvaluationDate
    rate_value: CurrencyExchangeRateRateValue


@dataclass(frozen=True)
class CurrencyId:
    """Currency ID value object."""

    value: UUID

    def __post_init__(self) -> None:
        """Post init validations."""
        if not isinstance(self.value, UUID):
            raise CurrencyIdValidationError(
                message="Invalid UUID. It should be a UUID instance."
            )

    @classmethod
    def from_string(cls, value: str) -> CurrencyId:
        """Create a CurrencyId instance from a uuid string."""
        try:

            uuid = UUID(value)

        except ValueError as error:
            raise CurrencyIdValidationError(
                message=f"Invalid string uuid: {value}"
            ) from error

        return cls(value=uuid)


@dataclass(frozen=True)
class CurrencyCode:
    """Currency code value object."""

    value: str

    def __post_init__(self) -> None:
        """Post init validations."""
        if len(self.value) > 3:
            raise CurrencyCodeLenghtValidationError(
                message="Max Currency code lenght: 3"
            )


@dataclass(frozen=True)
class CurrencyName:
    """CurrencyName value object."""

    value: str

    def __post_init__(self) -> None:
        """Post init validations."""
        if len(self.value) > 20:
            raise CurrencyNameLenghtValidationError(
                message="Max Currency name lenght: 20"
            )


@dataclass(frozen=True)
class CurrencySymbol:
    """Currency Symbol value object."""

    value: str

    def __post_init__(self) -> None:
        """Post init validations."""
        if len(self.value) > 3:
            raise CurrencySymbolLenghtValidationError(message="Max Symbol lenght: 3")


class Currency:
    """Currency model class."""

    _code: CurrencyCode
    _name: CurrencyName
    _symbol: CurrencySymbol

    def __init__(
        self, code: CurrencyCode, name: CurrencyName, symbol: CurrencySymbol
    ) -> None:
        """Currency class constructor."""
        self._code = code
        self._name = name
        self._symbol = symbol

    @property
    def code(self) -> CurrencyCode:
        """
        Return the Currency code.

        Returns
            CurrencyCode: CurrencyCode value object
        """
        return self._code

    @property
    def name(self) -> CurrencyName:
        """
        Return the Currency name.

        Returns
            CurrencyName: CurrencyName value object
        """
        return self._name

    @property
    def symbol(self) -> CurrencySymbol:
        """
        Return the Currency symbol.

        Returns
            CurrencySymbol: CurrencySymbol value object
        """
        return self._symbol
