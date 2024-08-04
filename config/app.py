"""App configuration"""

from core.facades.env import env, bool_env, int_env
from app.handler import Handler
from app.provider import AppProvider

config = {
    # Application URL"""
    "url": env('APP_URL', 'http://localhost:8000'),

    # Application name
    "name": env('APP_NAME', 'app'),

    # Application environment, development, testing, production
    "environment": env('ENVIRONMENT', 'development'),

    # Debug mode, only used in development
    "debug": bool_env('DEBUG', 'False'),

    # Debug port, only used in development
    "debug_port": int_env('DEBUG_PORT', '5666'),

    # Hot reload
    "hot_reload": bool_env('HOT_RELOAD', 'False'),

    # Number of processes to run the application
    "number_processes": int_env('NUMBER_PROCESSES', '1'),

    # Application exception handler
    "exception_handler": Handler,

    # Application providers
    # they will be registered in the container and booted in the same order
    "providers": [
        AppProvider,
    ]
}
