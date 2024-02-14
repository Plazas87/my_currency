"""Domain exception errors module."""


class DomainError(Exception):
    """Base class for Domain Exceptions."""

    def __init__(self, message: str) -> None:
        """Class constructor."""
        self.message = message
        super().__init__(self.message)


class CurrencyIdValidationError(DomainError):
    """CurrencyIdValidation error."""


class CurrencyCodeLenghtValidationError(DomainError):
    """CurrencyCodeLenghtValidation error."""


class CurrencyNameLenghtValidationError(DomainError):
    """CurrencyNameLenghtValidation error."""


class CurrencySymbolLenghtValidationError(DomainError):
    """CurrencySymbolLenghtValidation error."""


class CurrencyExchangeRateIdError(DomainError):
    """CurrencyExchangeRateId error."""


class CurrencyExchangeRateSourceCurrencyError(DomainError):
    """CurrencyExchangeRateSourceCurrency error."""


class CurrencyExchangeRateExchangeCurrencyError(DomainError):
    """CurrencyExchangeRateExchangeCurrency error."""


class CurrencyExchangeRateEvaluationDateError(DomainError):
    """CurrencyExchangeRateEvaluationDate error."""


class CurrencyExchangeRateRateValueError(DomainError):
    """CurrencyExchangeRateRateValue error."""
