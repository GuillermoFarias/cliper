""" Http Facade """
from typing import Type
from core.facades.app import App
from core.http.router import Router as HttpRouter


class Router:
    """ Router Facade. """

    @staticmethod
    def get(route: str, controller: Type, method_name: str):
        """ Register a GET route with a callback. """
        http_router: HttpRouter = App.make(HttpRouter)
        class_instance = controller()
        method_without_execute = getattr(class_instance, method_name)
        http_router.get(route, method_without_execute)

    @staticmethod
    def post(route: str, controller: Type, method_name: str):
        """ Register a POST route with a controller method. """
        http_router: HttpRouter = App.make(HttpRouter)
        class_instance = controller()
        method_without_execute = getattr(class_instance, method_name)
        http_router.post(route, method_without_execute)

    @staticmethod
    def put(route: str, controller: Type, method_name: str):
        """ Register a PUT route with a controller method. """
        http_router: HttpRouter = App.make(HttpRouter)
        class_instance = controller()
        method_without_execute = getattr(class_instance, method_name)
        http_router.put(route, method_without_execute)

    @staticmethod
    def delete(route: str, controller: Type, method_name: str):
        """ Register a DELETE route with a controller method. """
        http_router: HttpRouter = App.make(HttpRouter)
        class_instance = controller()
        method_without_execute = getattr(class_instance, method_name)
        http_router.delete(route, method_without_execute)
