""" Abstract class to implement connection for queue server. """
import abc
from typing import Callable


class Driver(abc.ABC):
    """ Abstract class to implement connection for queue server. """

    @abc.abstractmethod
    async def connect(self, name: str) -> None:
        """ Connect to the server."""

    @abc.abstractmethod
    def subscribe(self, queue_name: str, callback: Callable) -> None:
        """ Set the callback for incomming messages."""

    @abc.abstractmethod
    async def dispatch(self, queue_name: str, message) -> None:
        """ Send a message to the queue."""

    @abc.abstractmethod
    async def close(self):
        """ Close the connection."""
