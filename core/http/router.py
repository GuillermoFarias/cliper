""" This module provides a simple way to add routes to a FastAPI app """
from typing import Any, Callable
from fastapi import APIRouter
from fastapi.routing import APIRoute


class Router:
    """ Router class to add routes to a FastAPI app """

    def __init__(self):
        self._router = APIRouter()

    def add_route(self, method: str, path: str, callback: Callable, **kwargs: Any) -> None:
        """
        Add a route to the FastAPI app with request injection

        Args:
            method (str): HTTP method for the route (GET, POST, PUT, DELETE)
            path (str): URL path for the route
            controller (Type): Controller class
            method_name (str): Method name in the controller
            **kwargs (Any): Additional keyword arguments to pass to APIRoute
        """
        allowed_methods = ["GET", "POST", "PUT", "DELETE"]
        if method.upper() not in allowed_methods:
            raise ValueError(
                f"Invalid HTTP method: {method}. Allowed methods are: {', '.join(allowed_methods)}"
            )

        route = APIRoute(
            path=path,
            endpoint=callback,
            methods=[method.upper()]
        )
        self._router.routes.append(route)

    def get(self, path: str, callback: Callable) -> None:
        """ Add a GET route to the FastAPI app """
        self.add_route("GET", path, callback)

    def post(self, path: str, callback: Callable) -> None:
        """ Add a POST route to the FastAPI app """
        self.add_route("POST", path, callback)

    def put(self, path: str, callback: Callable) -> None:
        """ Add a PUT route to the FastAPI app """
        self.add_route("PUT", path, callback)

    def delete(self, path: str, callback: Callable) -> None:
        """ Add a DELETE route to the FastAPI app """
        self.add_route("DELETE", path, callback)

    def get_router(self):
        """ Get the FastAPI router """
        return self._router
