""" Redis cache module """
from redis.asyncio import Redis


class Cache:
    """Redis cache module"""

    def __init__(self):
        self.redis = None

    def connect(self, redis_host: str, redis_port: int, redis_password: str = None):
        """Connect to Redis"""
        self.redis = Redis(host=redis_host, port=redis_port, password=redis_password)

    async def set(self, key: str, value: str):
        """Set a key-value pair"""
        await self.redis.set(key, value)

    async def get(self, key: str):
        """Get a value by key"""
        data = await self.redis.get(key)
        return data.decode() if data else None

    async def delete(self, key: str):
        """Delete a key"""
        return await self.redis.delete(key)

    async def close(self):
        """Close the connection"""
        return await self.redis.close()
