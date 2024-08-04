# core/queue/drivers/redis.py
from typing import Callable, Awaitable
import json
import asyncio
import redis.asyncio as redis


class RedisQueueDriver:
    """ Redis Queue Connection Driver """

    def __init__(
            self,
            host: str,
            port: int = 6379,
            username: str = None,
            password: str = None
    ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None
        self.redis = None
        self.subscriber = None
        self.callback = None
        self.queue_name = None

    def set_on_subscribe(self, callback: Callable) -> None:
        """ Set the on subscribe callback """
        self.callback = callback

    async def connect(self, queue_name: str) -> None:
        """ Connect to Redis and set up subscription """
        try:
            self.queue_name = queue_name
            connection_string = f"redis://{self.host}:{self.port}"
            if self.password:
                connection_string += f"?password={self.password}"
            if self.password and self.username:
                connection_string += f"&username={self.username}"

            self.redis = redis.from_url(connection_string)
            self.subscriber = self.redis.pubsub()
            print(f"Connected to Redis: {self.host}:{self.port}")

            # subscribe to the queue
            await self.subscriber.subscribe(self.queue_name)
            asyncio.create_task(self._consume_messages())

        except Exception as e:
            print(f"Error connecting to Redis: {e}")

    def subscribe(self, queue_name: str, callback: Callable) -> None:
        """ Subscribe to a queue """
        self.queue_name = queue_name
        self.callback = callback

    async def close(self):
        """ Close the Redis connection """
        if self.redis:
            await self.redis.close()
        if self.subscriber:
            await self.subscriber.unsubscribe(self.queue_name)

    async def _consume_messages(self):
        """ Consume messages from Redis and invoke the callback """
        async for message in self.subscriber.listen():
            if message and message['type'] == 'message':
                data = json.loads(message['data'])
                job_name = data.get('job_name')
                job_data = data.get('job_data')
                if self.callback:
                    await self.callback(job_name, job_data)

    async def publish(self, job_name: str, job_data: dict) -> Awaitable:
        """ Enqueue a message to Redis """
        if not self.redis:
            raise ValueError("Connection not established")

        serialized_message = json.dumps({
            'job_name': job_name,
            'job_data': job_data
        })
        return await self.redis.publish(self.queue_name, serialized_message)
