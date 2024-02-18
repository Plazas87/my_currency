"""Dependecy injection factories module."""
import logging

from ..config import settings
from ..io.executors import HTTPExecutor, HTTPRequestValidator, HTTPResponseValidator

logger = logging.getLogger(__name__)


def http_executor_factory() -> HTTPExecutor:
    """Build and return a HTTPExecutor instance."""
    return HTTPExecutor(
        request_validator=HTTPRequestValidator(
            available_http_methods=settings.HTTP_EXECUTOR_ALLOWED_METODS
        ),
        response_validator=HTTPResponseValidator(),
    )
