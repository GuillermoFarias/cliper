""" Mongo Connector """
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ReadPreference


class MongoDBConnector:
    """ A MongoDB connector class that handles the connection to the database. """

    def __init__(self, uri: str, max_pool_size: int = 100):
        self.uri = uri
        self.max_pool_size = max_pool_size
        self.client = None
        self.db = None

    async def connect(self):
        """Establish a connection to MongoDB."""
        self.client = AsyncIOMotorClient(
            self.uri,
            maxPoolSize=self.max_pool_size,
            read_preference=ReadPreference.PRIMARY
        )
        self.db = self.client.get_default_database()

    async def close(self):
        """Close the connection to MongoDB."""
        if self.client:
            self.client.close()

    def get_collection(self, collection_name: str):
        """Get a collection from the database."""
        if self.db is not None:
            return self.db.get_collection(collection_name)
        else:
            raise RuntimeError("Database connection not established")

    def get_connection(self):
        """Get the database connection."""
        return self.client
