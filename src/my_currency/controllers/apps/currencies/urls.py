"""Currencies URLS paterns module."""
from django.urls import path

from my_currency.controllers.apps.currencies.views import GetCurrenciesByPeriodView

urlpatterns = [
    path("get_currencies_by_period/", GetCurrenciesByPeriodView.as_view()),
]
