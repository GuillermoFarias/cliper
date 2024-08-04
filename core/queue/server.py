""" Queue Server Module """
from typing import Callable
from core.queue.contracts.driver import Driver


class Server:
    """ Queue Server"""

    def __init__(self, connection_name: str, driver: Driver):
        self.connection_name = connection_name
        self.driver = driver

    async def start(self) -> None:
        """ Connect to the AMQP server."""
        await self.driver.connect(self.connection_name)

    def subscribe(self, queue_name: str, callback: Callable) -> None:
        """ Subscribe to a queue."""
        self.driver.subscribe(queue_name, callback)

    async def publish(self, queue_name: str, message: str):
        """ Publish a message to a queue."""
        return await self.driver.publish(queue_name, message)

    async def close(self) -> None:
        """ Close the connection."""
        await self.driver.close()
