""" Database provider """

from core.contracts.provider import Provider
from core.container import Container
from core.facades.config import config
from core.database.connector import MongoDBConnector


class DatabaseProvider(Provider):
    """ Database provider. """

    def register(self, container: Container) -> None:
        """Method to register dependencies."""
        database_config = config('database', 'database_uri')
        database_max_pool_size = config('database', 'max_pool_size', 100)

        database: MongoDBConnector = MongoDBConnector(database_config, database_max_pool_size)
        container.singleton(MongoDBConnector, database)

    async def boot(self, container: Container) -> None:
        """Method to boot the provider."""
        database: MongoDBConnector = container.make(MongoDBConnector)
        await database.connect()
