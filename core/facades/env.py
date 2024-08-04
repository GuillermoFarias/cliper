""" Facade for environment variable. """
from core.facades.app import App
from core.env import Environment


def env(key, default=None):
    """Get environment variable."""
    environment = App.make_optional(Environment, Environment())
    return environment.get(key, default)


def int_env(key, default=None):
    """Get environment variable."""
    environment = App.make_optional(Environment, Environment())
    return environment.int(key, default)


def bool_env(key, default=None):
    """Get environment variable."""
    environment = App.make_optional(Environment, Environment())
    return environment.bool(key, default)


def get_app_url():
    """Get the app URL."""
    environment = App.make_optional(Environment, Environment())
    return environment.get_app_url()
