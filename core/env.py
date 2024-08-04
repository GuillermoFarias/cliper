"""Environment variables."""
from environs import Env


class Environment:
    """Environment class."""

    def __init__(self):
        self._env = Env()
        self._env.read_env()
        self.app_url = self.get('APP_URL')

    def load(self, environment_name: str):
        """Load environment variables."""
        self._env.read_env(environment_name, override=True)

    def get(self, key: str, default=None):
        """Get environment variable."""
        return self._env(key, default=default)

    def int(self, key: str, default=None):
        """Get environment variable."""
        return self._env.int(key, default=default)

    def bool(self, key: str, default=None):
        """Get environment variable."""
        return self._env.bool(key, default=default)

    def get_app_url(self):
        """Get the app URL."""
        return self.app_url