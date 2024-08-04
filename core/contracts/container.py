"""Abstract container class."""
from abc import ABC, abstractmethod


class Container(ABC):
    """Container class."""

    @staticmethod
    def get_instance() -> 'Container':
        """Gets the instance of the container."""

    @abstractmethod
    def has(self, key):
        """Check if the container has a binding."""

    @abstractmethod
    def bind(self, key, cls):
        """Link a class to the container."""

    @abstractmethod
    def make(self, cls):
        """Obtains an instance from the container."""

    @abstractmethod
    def singleton(self, cls, instance):
        """Register a singleton object."""
