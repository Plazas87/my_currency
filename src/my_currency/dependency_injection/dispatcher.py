"""Dispatcher module."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class ICommand(ABC):
    """Command class."""


class IHandler(ABC):
    """Handler class."""

    @abstractmethod
    def handle(self, command: ICommand) -> Any:
        """Handle a command."""


@dataclass
class Dispatcher:
    """Dispatcher class."""

    _handlers: Dict[type[ICommand], IHandler]

    def __init__(self, handlers: Dict[type[ICommand], IHandler]) -> None:
        """Dispacher class constructor."""
        self._handlers = handlers

    def dispatch(self, command: ICommand) -> Optional[Any]:
        """Dispatch the command to his handler."""
        logger.debug("Start dispatching the command: '%s'", command)
        command_handler = self._handlers.get(type(command))
        if command_handler:
            result = command_handler.handle(command=command)
            logger.debug("Command '%s' successfully dispatched.", command)

            return result

        return None

    def __hash__(self) -> int:
        """
        Return the hash based on the command_handlers attribute.

        Returns
            int: hash
        """
        return hash(self._handlers)
