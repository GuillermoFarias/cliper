"""Admin handler for exceptions."""
import sys
import asyncio
from core.logging.logger import Logger
from core.contracts.handler import Handler


class DefaultExceptionHandler:
    """Exception class for the application."""
    logger: Logger = None
    app_handler: Handler = None

    def __init__(self, logger, app_handler=None):
        self.logger = logger
        self.app_handler = app_handler

    def handle_exception(self, exc_type, exc_value, exc_traceback) -> None:
        """Handle an exception."""
        self.log(exc_type, exc_value, exc_traceback)

        exception = self.reconstruct_exception(
            exc_type,
            exc_value,
            exc_traceback
        )

        if self.app_handler:
            self.app_handler.handle_exception(exception)

        loop = asyncio.get_event_loop()
        loop.stop()
        sys.exit(1)

    def log(self, exc_type, exc_value, exc_traceback):
        """Log the exception."""
        self.logger.log_exception(exc_type, exc_value, exc_traceback)

    def reconstruct_exception(self, exc_type, exc_value, exc_traceback):
        """ Reconstruct the exception."""
        exception = exc_type(exc_value)
        exception.__traceback__ = exc_traceback
        return exception

    def set_handler(self, app_handler: Handler):
        """Set the application handler."""
        self.app_handler = app_handler
