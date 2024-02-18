"""Application services module."""

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")
S = TypeVar("S")
K = TypeVar("K")
V = TypeVar("V")


class RequestValidator(ABC, Generic[T]):  # pylint: disable=R0903
    """RequestValidator Abstract base class."""

    @abstractmethod
    def validate(self, obj: T) -> None:
        """
        Validate a request.

        Args:
            obj (Request): Resquest to validate.

        """


class ResponseValidator(ABC, Generic[T]):  # pylint: disable=R0903
    """ResponseValidator Abstract base class."""

    @abstractmethod
    def validate(self, obj: T) -> None:
        """
        Validate a response.

        Args:
            obj (Response): Response to validate.

        """


class IExecutor(ABC, Generic[T, S]):  # pylint: disable=too-few-public-methods
    """Executor Abstrac class."""

    @abstractmethod
    async def execute(self, request: T) -> S:
        """
        Execute a request.

        Args:
            request (Request): contains the information to perform the request

        Returns
            Response: request response
        """


class IRepository(ABC, Generic[V, K, T]):
    """Interface for the repositories."""

    @staticmethod
    @abstractmethod
    def generate_uuid() -> K:
        """Generate an uuid."""

    @abstractmethod
    def save(self, obj: V) -> T:
        """Save an obj in the database."""

    @abstractmethod
    def save_bulk(self, objs: List[V]) -> T:
        """Save a list of objs in the database."""

    @abstractmethod
    def update(self, obj: V) -> T:
        """Update an obj in the database."""


class IExchangeCurrenteRateFinder(ABC, Generic[V, K]):
    """Interface for finders."""

    @abstractmethod
    def get_by_source_currency_and_date_period(
        self, source_currency: V, date_from: V, date_to: V
    ) -> List[K]:
        """Get Exchange currencies rates by source currency and period."""


class IProvidersFinder(ABC, Generic[V, K]):
    """Provider finder interface."""

    @abstractmethod
    def get_by_name(self, name: V) -> Optional[K]:
        """Get an instance by its name."""

    # @abstractmethod
    # def get_all(self) -> List[K]:
    #     """Get all available objs."""
    #     # this method sould be used with caution. Database table could be
    #     # big enough to crash the application.

    # @abstractmethod
    # def exists(self, name: V) -> T:
    #     """Check if the instance exists in the database."""


class ICurrencyFinder(ABC, Generic[V, K]):
    """Currency finder interface."""

    @abstractmethod
    def get_by_code(self, code: V) -> Optional[K]:
        """Get an instance by its name."""


class IProvider(ABC, Generic[S, T, V]):
    """Provider Interface."""

    @property
    @abstractmethod
    def priority(self) -> V:
        """Return the priority."""

    @abstractmethod
    def get_currencies(
        self,
        source_currency: S,
        valuation_date: S,
        exchange_courrency: Optional[S] = ...,
    ) -> List[T]:
        """Get currencies for a valuation date."""

    # @abstractmethod
    # def get_currencies_timeseries(self, source_currency: S, date_from: V, date_to: V) -> T:
    #     """Get currency timeseries from a period."""


class IProviderManager(ABC, Generic[V]):
    """Provider Manager interface."""

    @abstractmethod
    def get_providers(self) -> List[V]:
        """Get all available providers."""


class ITimeSeriesGenerator(ABC, Generic[K]):
    """TimeSeriesGenerator interface."""

    @staticmethod
    @abstractmethod
    def generate(start_date: K, end_date: K) -> List[K]:
        """Generate a daily timeseries for a period."""


class ISerializer(ABC, Generic[K, V]):
    """ISerializer interface."""

    def serialize(self, obj: K) -> V:
        """Transform a ExchangeRatesResponse to a CurrencyExchangeRateDTO."""
