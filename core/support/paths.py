"""This module contains helper functions for the framework."""
import os


def core_path():
    """Get the core path."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def root_path():
    """Get the root path of the project."""
    return os.path.dirname(core_path())


def app_path():
    """Get the app path."""
    return os.path.join(root_path(), 'app')


def config_path():
    """Get the config path."""
    return os.path.join(root_path(), 'config')


def routes_path():
    """Get the routes path."""
    return os.path.join(root_path(), 'routes')


def database_path():
    """Get the database path."""
    return os.path.join(app_path(), 'database')


def database_migrations_path():
    """Get the migrations path."""
    return os.path.join(database_path(), 'migrations')


def database_seeds_path():
    """Get the seeds path."""
    return os.path.join(database_path(), 'seeds')


def storage_path():
    """Get the storage path."""
    return _add_path(root_path(), 'storage')


def cache_path(path: str = ''):
    """Get the cache path."""
    return _add_path(storage_path(), _add_path('cache', path))


def _add_path(original_path: str, path: str = None):
    """Add a path to the original path."""
    if path is None:
        return original_path

    return os.path.join(original_path, path)
