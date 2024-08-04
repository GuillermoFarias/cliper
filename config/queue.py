""" Http configuration """
from core.facades.env import env
from core.support.paths import routes_path

config = {
    "queue": env('REDIS_QUEUE', env('APP_NAME', 'app')),
    "port": int(env('REDIS_PORT', 6379)),
    "host": env('REDIS_HOST', 'localhost'),
    "password": env('REDIS_PASSWORD', 'guest'),
    "path": routes_path(),
    "routers": [
        "jobs.py",
    ]
}
