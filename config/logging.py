"define logging configuration"

from core.facades.env import env

default_channel = env("LOG_CHANNEL", "default")

channels = {
    "default": {
        "path": "storage/app.log",
        "level": "INFO",
        "format": "default",
    },
}

formatters = {
    "default":  "[%(asctime)s] [%(levelname)s] %(message)s"
}
