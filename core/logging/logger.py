import logging
from logging.handlers import RotatingFileHandler


class Logger:
    """Logger class for the application."""

    ERROR = logging.ERROR
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    WARNING = logging.WARNING

    def __init__(self, channels: dict, formatters: dict, default_channel="default"):
        self.channels = channels
        self.formatters = formatters
        self.default_channel = default_channel
        self.default_formatter = "default"
        self.logger = None

    def setup_logging(self, channel=None) -> logging.Logger:
        """Configure logging based on settings."""
        if self.logger:
            return self.logger

        channel = channel or self.default_channel
        config = self.channels.get(channel, {})
        formatter_pattern = self.formatters.get(
            config.get("format", self.default_formatter),
            self.formatters[self.default_formatter]
        )
        log_file = config.get("path", "storage/logs/app.log")
        level = config.get("level", "INFO").upper()

        self.logger = logging.getLogger(channel)
        self.logger.setLevel(getattr(logging, level, logging.INFO))
        self.logger.handlers = []

        formatter = logging.Formatter(formatter_pattern)
        file_handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
        file_handler.setLevel(getattr(logging, level, logging.INFO))
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

        return self.logger

    def log(self, message, level=logging.INFO, channel=None):
        """Log a message with the specified level."""
        logger = self.setup_logging(channel)
        logger.log(level, message)

    def log_exception(self, exc_type, exc_value, exc_traceback):
        """Log an exception with traceback."""
        error_file = exc_traceback.tb_frame.f_code.co_filename \
            or exc_traceback.tb_frame.f_globals.get("__file__")
        error_line = exc_traceback.tb_lineno or exc_traceback.tb_frame.f_lineno

        logger = self.setup_logging(self.default_channel)
        exception_formatter = logging.Formatter(
            self.formatters[self.default_formatter] +
            f"\nFile:Line ({error_file}:{error_line})"
        )
        for handler in logger.handlers:
            handler.setFormatter(exception_formatter)
        logger.error(exc_value, exc_info=(exc_type, exc_value, exc_traceback))
        self.write("\n")

    def set_level(self, level):
        """Set the logging level for the logger."""
        logger = self.setup_logging()
        logger.setLevel(level)

    def write(self, message: str, channel=None):
        """Write a message to the log."""
        logger = self.setup_logging(channel)
        logger.info(message)
