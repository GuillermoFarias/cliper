""" This module defines the Provider contract. """
import abc
from core.contracts.container import Container


class Provider(abc.ABC):
    """Abstract class for defining a provider."""

    def register(self, container: Container) -> None:
        """Method to register dependencies."""

    async def boot(self, container: Container) -> None:
        """Method to boot the provider."""
