""" Cache provider """

from core.contracts.provider import Provider
from core.container import Container
from core.facades.config import config
from core.cache.cache import Cache


class CacheProvider(Provider):
    """ Cache provider. """

    def register(self, container: Container) -> None:
        """Method to register dependencies."""
        cache = Cache()
        container.singleton(Cache, cache)

    async def boot(self, container: Container) -> None:
        """Method to boot the provider."""
        host = config('cache', 'host', 'localhost')
        port = int(config('cache', 'port', 6379))
        password = config('cache', 'password', None)

        cache: Cache = container.make(Cache)
        cache.connect(host, port, password)
