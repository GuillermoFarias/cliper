""" Bootstraps all the application components. """
import asyncio

from core.contracts.container import Container as ContainerContract
from core.contracts.provider import Provider
from core.container import Container
from core.facades.config import config
from core.providers.logging import LoggingProvider
from core.providers.exception import ExceptionProvider
from core.providers.queue import QueueProvider
from core.providers.http import HttpProvider
from core.providers.cache import CacheProvider
from core.providers.database import DatabaseProvider


class App:
    """ Application bootstrapper. """

    def __init__(self, container: ContainerContract = None):
        """ Constructor """
        self.container = container or Container.get_instance()

    def boot(self):
        """Initializes the application."""
        # Register all
        loop = asyncio.get_event_loop()
        loop.create_task(self._boot_async())
        loop.run_forever()

    def _get_core_providers(self) -> list[Provider]:
        """ Get all the core providers. """
        return [
            DatabaseProvider,
            HttpProvider,
            LoggingProvider,
            ExceptionProvider,
            QueueProvider,
            CacheProvider,
        ]

    def _get_app_providers(self) -> list[Provider]:
        """ Get all the app providers. """
        return config('app', 'config.providers', [])

    async def _boot_async(self):
        """ Bootstraps the application asynchronously."""
        app_providers = self._get_app_providers()
        core_providers = self._get_core_providers()

        # Register all the providers
        for provider in core_providers + app_providers:
            provider().register(self.container)

        # Boot app providers
        for provider in app_providers:
            await provider().boot(self.container)

        # Boot core providers
        await asyncio.gather(*[provider().boot(self.container) for provider in core_providers])