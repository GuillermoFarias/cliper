""" Exception provider """
import sys
from core.contracts.provider import Provider
from core.container import Container
from core.exception.exception import DefaultExceptionHandler
from core.logging.logger import Logger
from core.facades.config import config


class ExceptionProvider(Provider):
    """ Exception provider. """

    def register(self, container: Container) -> None:
        """Method to register dependencies."""
        logger = container.make(Logger)
        app_handler_class = config('app', 'config.exception_handler')

        handler = DefaultExceptionHandler(logger, app_handler_class())
        sys.excepthook = handler.handle_exception
