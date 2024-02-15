"""Currencies app configuration module."""
from django.apps import AppConfig


class CurrenciesConfig(AppConfig):
    """Currencies configuration class."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "my_currency.controllers.apps.currencies"
    verbose_name = "Currencies"
    label = "currencies"
