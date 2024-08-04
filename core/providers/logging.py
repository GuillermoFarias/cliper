""" Logging provider """
from core.contracts.provider import Provider
from core.container import Container
from core.logging.logger import Logger
from core.facades.config import config


class LoggingProvider(Provider):
    """ Logging provider. """

    def register(self, container: Container) -> None:
        """Method to register dependencies."""

        channels = config('logging', 'channels')
        formatters = config('logging', 'formatters')
        default_channel = config('logging', 'default_channel', 'default')

        logger = Logger(channels, formatters, default_channel)

        container.singleton(Logger, logger)
