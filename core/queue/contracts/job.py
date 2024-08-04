""" Contracts for jobs. """
import asyncio
from abc import ABC, abstractmethod
from core.facades.app import App
from core.queue.server import Server


class Job(ABC):
    """Abstract base class for jobs."""
    job_data: dict = {}

    @abstractmethod
    async def handle(self, data: dict) -> None:
        """Execute the job."""
        print("Job handle method not implemented.")

    def get_idenfier(self) -> str:
        """Get the job identifier."""
        return self.__class__.__name__

    def get_data(self) -> dict:
        """Get the job data."""
        return self.job_data

    def set_data(self, data: dict) -> None:
        """Set the job data."""
        self.job_data = data

    @classmethod
    async def dispatch(cls, data: dict) -> None:
        """Dispatch the job."""
        identifier: str = cls.__name__
        queue_server: Server = App.make(Server)
        return await queue_server.publish(identifier, data)

    @classmethod
    async def dispatch_async(cls, data: dict) -> None:
        """Dispatch the job asynchronously."""
        asyncio.create_task(cls.dispatch(data))
