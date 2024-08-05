""" Url Access Log Repository """
from app.models.url_access_log import UrlAccessLog
from core.database.repository import MongoDBRepository
from core.database.connector import MongoDBConnector


class UrlAccessLogRepository:
    """ Url Access Log Repository """

    def __init__(self, connector: MongoDBConnector):
        """ Constructor """
        self.connector = connector
        self.repository = MongoDBRepository(self.connector, UrlAccessLog, 'urls_access_log')

    async def create(self, model: UrlAccessLog) -> UrlAccessLog:
        """ Create a new URL """
        return await self.repository.create(model)

    async def find_by_id(self, _id: str) -> UrlAccessLog:
        """ Find a URL by short URL """
        return await self.repository.read(_id)

    async def delete(self, model: UrlAccessLog) -> None:
        """ Delete a URL """
        await self.repository.delete(model.id)
