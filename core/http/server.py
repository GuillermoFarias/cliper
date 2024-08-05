"""This is the main file for the server. It is responsible for handling all"""
from typing import Callable
import asyncio
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
import uvicorn


class Server:
    """Server module for the application."""

    def __init__(self, port: int, host: str, workers: int = 10, log_level: str = "info"):
        self.port = port
        self.host = host
        self.workers = workers
        self.log_level = log_level
        self.routers = []
        self.exception_handler = None
        self.validation_exception_handler = None

    def add_router(self, router: APIRouter):
        """Add a router to the server."""
        self.routers.append(router)

    def register_exception_handler(self, handler: Callable) -> None:
        """Register an exception handler for the server."""
        self.exception_handler = handler

    def register_validation_exception_handler(self, handler: Callable) -> None:
        """Register a validation exception handler for the server."""
        self.validation_exception_handler = handler

    def start_server(self, api: FastAPI = None):
        """Start the server."""
        api.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        for router in self.routers:
            api.include_router(router)

        if self.exception_handler:
            api.add_exception_handler(Exception, self.exception_handler)

        if self.validation_exception_handler:
            api.add_exception_handler(RequestValidationError, self.validation_exception_handler)

        # Use a new asyncio task to run uvicorn
        asyncio.ensure_future(self._run_server(api))

    async def _run_server(self, api: FastAPI):
        """Run the server in an asyncio task."""
        config = uvicorn.Config(api,
                                host=self.host,
                                port=self.port,
                                log_level=self.log_level,
                                workers=self.workers
                                )
        server = uvicorn.Server(config)
        await server.serve()
