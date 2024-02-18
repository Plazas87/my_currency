"""Currencies views module."""

import logging
from dataclasses import asdict
from http import HTTPStatus

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from my_currency.application.commands import GetCurrencyRatesByPeriodCommand
from my_currency.application.responses import HTTPResponse
from my_currency.dependency_injection.container import container

logger = logging.getLogger(__name__)


class GetCurrenciesByPeriodView(APIView):
    """GetCurrenciesByPeriod class based view."""

    # Skip login
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """Handle a GET request."""
        print()
        return Response({})

    def post(self, request) -> Response:
        """Return a number list."""
        response_data = {"status_code": HTTPStatus.OK, "headers": {}, "body": {}}

        try:
            get_currencies_by_period_command = GetCurrencyRatesByPeriodCommand(
                **request.data
            )
            rates = container.dispatcher.dispatch(
                command=get_currencies_by_period_command
            )
            response_data.update(
                {"body": {"rates": [asdict(exchange_rate) for exchange_rate in rates]}}
            )

        except Exception as error:
            logger.error("%s", error)
            response_data.update(
                {
                    "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
                    "body": {"error": "Unhandled error."},
                }
            )

        return Response(asdict(HTTPResponse(**response_data)))


# Create your views here.


# {
#     "source_currency": "EUR",
#     "date_from":"2024-02-10" ,
#     "date_to": "2024-02-11"
# }
