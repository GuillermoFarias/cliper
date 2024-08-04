""" Queue provider """
import importlib.util
import os

from core.contracts.provider import Provider
from core.container import Container
from core.facades.config import config
from core.queue.router import Router
from core.queue.server import Server
from core.queue.drivers.redispy import RedisQueueDriver


class QueueProvider(Provider):
    """ Queue provider. """

    def register(self, container: Container) -> None:
        """Method to register dependencies."""
        queue_router = Router()
        container.singleton(Router, queue_router)

        http_config = config('queue', 'config', {})
        routers = http_config.get('routers', [])
        path = http_config.get('path', '')

        for router in routers:
            route_file = os.path.join(path, router)
            if os.path.isfile(route_file):
                spec = importlib.util.spec_from_file_location(router, route_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

    async def boot(self, container: Container) -> None:
        """Method to boot the provider."""
        queue_config = config('queue', 'config', {})
        queue_name = queue_config.get('name', 'default')
        user = queue_config.get('user', 'guest')
        password = queue_config.get('password', 'guest')
        port = int(queue_config.get('port', 5672))
        host = queue_config.get('host', 'localhost')

        driver = RedisQueueDriver(host, port, user, password)
        queue_router: Router = container.make(Router)
        server = Server('app_1', driver)
        server.subscribe(queue_name, queue_router.process_job)
        container.singleton(Server, server)
        await server.start()
