"""Providers admin module."""
from django.contrib import admin

from my_currency.controllers.apps.providers.models import Provider

admin.site.register(Provider)
