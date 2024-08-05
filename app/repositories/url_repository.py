""" URL Repository """
from app.models.url import Url
from core.database.repository import MongoDBRepository
from core.database.connector import MongoDBConnector


class UrlRepository:
    """ URL Repository """

    def __init__(self, connector: MongoDBConnector):
        """ Constructor """
        self.connector = connector
        self.repository = MongoDBRepository(self.connector, Url, 'urls')

    async def create(self, url: Url) -> Url:
        """ Create a new URL """
        return await self.repository.create(url)

    async def find_by_short_id(self, short_id: str) -> Url:
        """ Find a URL by short URL """
        return await self.repository.find_one({'short_id': short_id})

    async def create_index(self) -> None:
        """ Create indexes """
        await self.repository.create_index('short_id')

    async def delete(self, url: Url) -> None:
        """ Delete a URL """
        await self.repository.delete(url.id)
