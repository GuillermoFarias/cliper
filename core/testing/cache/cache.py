""" Cache Test module """


class Cache:
    """Redis cache module"""

    def __init__(self):
        self.data = {}

    async def set(self, key: str, value: str):
        """Set a key-value pair"""
        self.data.update({key: value})

    async def get(self, key: str):
        """Get a value by key"""
        return self.data.get(key)

    async def delete(self, key: str):
        """Delete a key"""
        return self.data.pop(key, None)

    async def close(self):
        """Close the connection"""
        return True
