"""Handler contract."""
import abc


class Handler(abc.ABC):
    """Handler contract."""
    @abc.abstractmethod
    def handle_exception(self, exception: Exception) -> None:
        """Handle an exception."""
