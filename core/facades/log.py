""" This module provides a facade for the logger. """
from core.container import Container
from core.logging.logger import Logger


class Log:
    """Facade for the logger."""

    @staticmethod
    def info(message, channel=None):
        """Log a message with the INFO level."""
        logger: Logger = Container.get_instance().make(Logger)
        logger.log(message, channel=channel)

    @staticmethod
    def error(message, channel=None):
        """Log a message with the ERROR level."""
        logger: Logger = Container.get_instance().make(Logger)
        logger.log(message, level=logger.ERROR, channel=channel)

    @staticmethod
    def debug(message, channel=None):
        """Log a message with the DEBUG level."""
        logger: Logger = Container.get_instance().make(Logger)
        logger.log(message, level=logger.DEBUG, channel=channel)

    @staticmethod
    def warning(message, channel=None):
        """Log a message with the WARNING level."""
        logger: Logger = Container.get_instance().make(Logger)
        logger.log(message, level=logger.WARNING, channel=channel)

    @staticmethod
    def console(message):
        """Print a message."""
        print(message)
