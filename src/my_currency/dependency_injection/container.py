"""IoC Container."""

# pylint: disable=all

from django.conf import settings

from my_currency.application.commands import GetCurrencyRatesByPeriodCommand
from my_currency.application.handlers import GetCurrencyRatesByPeriodCommandHandler
from my_currency.application.services.exchange_rates_fetcher import (
    get_exchange_rate_data,
)
from my_currency.application.services.time_series_generators import (
    DailyTimeSeriesGenerator,
)
from my_currency.dependency_injection.dispatcher import Dispatcher
from my_currency.infrastructure.executors import (
    HTTPExecutor,
    HTTPRequestValidator,
    HTTPResponseValidator,
)
from my_currency.infrastructure.finders import (
    CurrencyExchangeRateFinder,
    CurrencyFinder,
    ProvidersFinder,
)
from my_currency.infrastructure.providers import (
    FixerProvider,
    MockProvider,
    ProviderManager,
)
from my_currency.infrastructure.repositories import CurrencyExchangeRateRepository
from my_currency.infrastructure.serializers import ExchangeRatesResponseSerializer


def get_available_http_methods():
    """Get available http methods."""
    return {i[0]: i[1] for i in settings.AVAILABLE_HTTP_METHODS}


available_http_methods = get_available_http_methods()
http_response_validator = HTTPResponseValidator()
http_request_validator = HTTPRequestValidator(
    available_http_methods=available_http_methods
)

executor = HTTPExecutor(
    request_validator=http_request_validator, response_validator=http_response_validator
)
exchange_rates_repository = CurrencyExchangeRateRepository()
currency_finder = CurrencyFinder()
exchange_rates_finder = CurrencyExchangeRateFinder()
provider_finder = ProvidersFinder()
exchange_rates_response_serializer = ExchangeRatesResponseSerializer()

external_exchange_rates_providers = {"Fixer": FixerProvider, "Mock": MockProvider}

provider_manager = ProviderManager(
    providers=external_exchange_rates_providers,
    request_executor=executor,
    provider_finder=provider_finder,
    available_symbols=settings.AVAILABLE_EXCHANGE_SYMBOLS,
)

days_between_generator = DailyTimeSeriesGenerator()


class Container:
    """Container with all the dependencies."""

    handlers = {
        GetCurrencyRatesByPeriodCommand: GetCurrencyRatesByPeriodCommandHandler(
            executor=executor,
            provider_manager=provider_manager,
            exchange_rates_repository=exchange_rates_repository,
            exchange_rates_finder=exchange_rates_finder,
            get_exchange_rate_data=get_exchange_rate_data,
            available_currency_symbols=available_http_methods,
            days_between_generator=days_between_generator,
            exchange_rates_response_serializer=exchange_rates_response_serializer,
            currency_finder=currency_finder,
        )
    }

    dispatcher = Dispatcher(handlers=handlers)


container = Container()
