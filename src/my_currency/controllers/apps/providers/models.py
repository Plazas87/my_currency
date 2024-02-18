"""Providers models module."""

import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


def get_available_http_methods():
    """Get available http methods."""
    return {i: i for i in settings.AVAILABLE_HTTP_METHODS}


class Provider(models.Model):
    """Provider model class."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    name = models.CharField(max_length=20)
    priority = models.IntegerField()
    method = models.CharField(max_length=6, choices=get_available_http_methods())
    url = models.URLField()
    access_key = models.CharField(max_length=300)

    class Meta:
        """Providers Meta class."""

        verbose_name = _("Provider")
        verbose_name_plural = _("Providers")
        ordering = ["priority"]

    def __str__(self) -> str:
        """Nice object string representation."""
        return f"{self.id}"

    def __repr__(self) -> str:
        """Nice object representation."""
        return (
            f"Provider("
            f"id={self.id}, "
            f"name={self.name}, "
            f"priority={self.priority}, "
            f"method={self.method}), "
            f"url={self.url})"
        )
