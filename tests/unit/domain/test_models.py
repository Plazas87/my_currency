"""Domain models tests module."""

from uuid import UUID

import pytest
from my_currency.domain.models.exceptions import (
    CurrencyCodeLenghtValidationError,
    CurrencyIdValidationError,
    CurrencyNameLenghtValidationError,
    CurrencySymbolLenghtValidationError,
)
from my_currency.domain.models.exchange_rates import (
    Currency,
    CurrencyCode,
    CurrencyId,
    CurrencyName,
    CurrencySymbol,
)


def test_currency_id_valid() -> None:
    # Arrange
    str_uuid = "123e4567-e89b-12d3-a456-426614174000"

    # expected value
    expected_value = UUID(str_uuid)

    # Act
    currency_id = CurrencyId.from_string("123e4567-e89b-12d3-a456-426614174000")

    # Asserts
    assert currency_id.value == expected_value


def test_currency_id_invalid() -> None:
    # Arrange

    # Act
    with pytest.raises(CurrencyIdValidationError) as error:
        CurrencyId.from_string("invalid-uuid")

    # Asserts
    assert error.value.message == "Invalid string uuid: invalid-uuid"


def test_currency_code_valid() -> None:
    # Arrange
    currency_code = "USD"

    # Act
    currency_code_result = CurrencyCode(currency_code)

    # Asserts
    assert currency_code_result.value == currency_code


def test_currency_code_invalid() -> None:
    # Arrange
    currency_code = "USDD"

    # Act
    with pytest.raises(CurrencyCodeLenghtValidationError) as error:
        CurrencyCode(currency_code)

    # Asserts
    assert error.value.message == "Max Currency code lenght: 3"


def test_currency_name_valid() -> None:
    # Arrange
    currency_name = "Dollar"

    # Act
    currency_name_result = CurrencyName(currency_name)

    # Asserts
    assert currency_name_result.value == currency_name


def test_currency_name_invalid() -> None:
    # Arrange
    currecy_name = "D" * 21
    # Act
    with pytest.raises(CurrencyNameLenghtValidationError) as error:
        CurrencyName(currecy_name)

    # Assert
    assert error.value.message == "Max Currency name lenght: 20"


def test_currency_symbol_valid() -> None:
    # Arrange
    currency_symbol = "EUR"

    # Act
    currency_symbol_result = CurrencySymbol(currency_symbol)

    # Assert
    assert currency_symbol_result.value == currency_symbol


def test_currency_symbol_invalid() -> None:
    # Arrange
    currency_symbol = "DNDS"
    # Act
    with pytest.raises(CurrencySymbolLenghtValidationError) as error:
        CurrencySymbol(currency_symbol)

    # Assert
    assert error.value.message == "Max Symbol lenght: 3"


def test_currency_model() -> None:
    # Arrange
    currecy_code = CurrencyCode("USD")
    currecy_name = CurrencyName("Dollar")
    currecy_symbol = CurrencySymbol("$")

    # Act
    currency = Currency(code=currecy_code, name=currecy_name, symbol=currecy_symbol)

    # Asserts
    assert currency.code.value == currecy_code.value
    assert currency.name.value == currecy_name.value
    assert currency.symbol.value == currecy_symbol.value
