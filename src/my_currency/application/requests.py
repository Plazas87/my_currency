"""Application data transfer object module."""
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class HTTPRequest:
    """Request data transfer object."""

    method: str
    url: str
    query_params: Optional[Dict[str, Any]] = None
    body: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, Any]] = None
