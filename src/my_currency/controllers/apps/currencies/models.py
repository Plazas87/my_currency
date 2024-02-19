"""Currencies models module."""
from __future__ import annotations

import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Currency(models.Model):
    """Currency model class."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=30, db_index=True)
    symbol = models.CharField(max_length=3)

    class Meta:
        """Currency Meta class."""

        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")
        ordering = ["code"]
        app_label = "currencies"

    def __str__(self) -> str:
        """Nice object string representation."""
        return f"{self.name}"

    def __repr__(self) -> str:
        """Nice object representation."""
        return f"Currency(id={self.id}, code={self.code}, name={self.name}, symbol={self.symbol})"


class CurrencyExchangeRate(models.Model):
    """Currency exchange rate model."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    source_currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="exchanges"
    )
    exchange_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    valuation_date = models.DateField(db_index=True)
    rate_value = models.DecimalField(db_index=True, decimal_places=6, max_digits=18)

    class Meta:
        """CurrencyExchangeRate Meta class."""

        verbose_name = _("CurrencyExchangeRate")
        verbose_name_plural = _("CurrencyExchangeRates")
        ordering = ["valuation_date"]
        app_label = "currencies"

    def __str__(self) -> str:
        """Nice object string representation."""
        return f"{self.id}"

    def __repr__(self) -> str:
        """Nice object representation."""
        return (
            f"CurrencyExchangeRate("
            f"id={self.id}, "
            f"source_currency={self.source_currency_id}, "
            f"exchange_currency={self.exchange_currency_id}, "
            f"valuation_date={self.valuation_date})"
        )
