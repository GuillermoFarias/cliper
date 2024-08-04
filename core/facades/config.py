
""" Facade for ConfigReader class. """
from core.config import Config
from core.support.paths import config_path


def config(config_file: str, key: str = None, default=None):
    """ Get config value. """
    config_reader = Config(config_path())
    value = config_reader.get(config_file, key)

    if value is None:
        return default

    return value
