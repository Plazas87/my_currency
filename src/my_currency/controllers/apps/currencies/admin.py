"""Currencies admin module."""
from django.contrib import admin

from .models import Currency, CurrencyExchangeRate


# Register your models here.
class CurrencyAdmin(admin.ModelAdmin):
    """CurrencyAdmin class."""

    def get_queryset(self, request):
        """Filter the admin query set by User."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(category__workspace__owner=request.user)


class CurrencyExchangeRateAdmin(admin.ModelAdmin):
    """CurrencyExchangeRateAdmin class."""

    def get_queryset(self, request):
        """Filter the admin query set by User."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(category__workspace__owner=request.user)


admin.site.register(Currency)
admin.site.register(CurrencyExchangeRate)
