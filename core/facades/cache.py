""" Cache Facade """
from core.cache.cache import Cache as CoreCache
from core.facades.app import App


class Cache:
    """ Cache Facade. """

    @staticmethod
    async def set(key: str, value: any):
        """ Set a value in the cache. """
        cache: CoreCache = App.make(CoreCache)
        await cache.set(key, value)

    @staticmethod
    async def get(key: str) -> any:
        """ Get a value from the cache. """
        cache: CoreCache = App.make(CoreCache)
        return await cache.get(key)

    @staticmethod
    async def delete(key: str):
        """ Delete a value from the cache. """
        cache: CoreCache = App.make(CoreCache)
        await cache.delete(key)
