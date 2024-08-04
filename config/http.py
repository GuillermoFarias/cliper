""" Http configuration """
from core.support.paths import routes_path

config = {
    "port": 8000,
    "host": "0.0.0.0",
    "path": routes_path(),
    "routers": [
        "api.py",
        "web.py",
    ],
    "log_level": "info",
    "workers": 10,
}
