""" App Facade. """
from core.container import Container


class App:
    """ App Facade."""

    @staticmethod
    def get_uri():
        """Get the database URI."""
        return Container.get_instance().get_app_base_url()

    @staticmethod
    def make(key):
        """Get an instance from the container."""
        return Container.get_instance().make(key)

    @staticmethod
    def make_optional(key, optional=None):
        """Get an instance from the container."""
        if optional:
            if Container.get_instance().has(key):
                return Container.get_instance().make(key)

            return optional

        return Container.get_instance().make(key)

    @staticmethod
    def bind(key, cls, *args, **kwargs):
        """Bind a class to the container."""
        def callback():
            return cls(*args, **kwargs)
        Container.get_instance().register(key, callback)

    @staticmethod
    def register(key, cls):
        """Register a class to the container."""
        Container.get_instance().register(key, cls)

    @staticmethod
    def singleton(key, cls, *args, **kwargs):
        """Register a class as a singleton."""
        def callback():
            return cls(*args, **kwargs)
        Container.get_instance().singleton(key, callback)
