""" Http provider """
import importlib.util
import os

from fastapi import FastAPI
from core.contracts.provider import Provider
from core.container import Container
from core.facades.config import config
from core.http.router import Router
from core.http.server import Server
from app.handler import Handler


class HttpProvider(Provider):
    """ Http provider. """

    def __init__(self):
        """ Constructor """
        self.api = FastAPI(
            title="Cliper API",
            description="API for Cliper URL shortener",
            version="1.0.0",
        )

    def register(self, container: Container) -> None:
        """Method to register dependencies."""

        http_router = Router()
        container.singleton(Router, http_router)
        container.singleton(FastAPI, self.api)

        http_config = config('http', 'config', {})
        routers = http_config.get('routers', [])
        path = http_config.get('path', '')

        # Read routers files
        for router in routers:
            route_file = os.path.join(path, router)
            if os.path.isfile(route_file):
                spec = importlib.util.spec_from_file_location(router, route_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

    async def boot(self, container: Container) -> None:
        """Method to boot the provider."""
        http_config = config('http', 'config', {})

        port = int(http_config.get('port', 8000))
        host = http_config.get('host', '0.0.0.0')
        workers = http_config.get('workers', 1)
        log_level = http_config.get('log_level', 'info')

        server = Server(port, host, workers, log_level)
        http_router: Router = container.make(Router)

        server.register_exception_handler(Handler().handle_api_exception)
        server.register_validation_exception_handler(Handler().handle_api_validation_exception)

        server.add_router(http_router.get_router())
        server.start_server(api=self.api)
