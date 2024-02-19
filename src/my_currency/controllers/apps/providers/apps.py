"""Providers app configuration module."""
from django.apps import AppConfig


class ProvidersConfig(AppConfig):
    """Providers configuration class."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "my_currency.controllers.apps.providers"
    verbose_name = "Providers"
    label = "providres"
