""" Save new url to database """
from app.models.url import Url
from app.repositories.url_repository import UrlRepository
from core.queue.contracts.job import Job
from core.support.inject import inject
from core.facades.cache import Cache


class CreateNewUrl(Job):
    """ Save new url to database """

    @inject
    def __init__(self, url_repository: UrlRepository):
        """ Constructor """
        self.url_repository = url_repository

    async def handle(self, data: dict) -> bool:
        """ Handle the process """
        orignal_url = data.get('url')
        short_id = data.get('short_id')
        url: Url = Url(url=orignal_url, short_id=short_id)

        await self.save_in_database(url)
        await self.save_in_cache(url)

        return True

    async def save_in_database(self, url: Url) -> None:
        """ Save the new URL in the database"""
        await self.url_repository.create_index()
        await self.url_repository.create(url)

    async def save_in_cache(self, url: Url) -> None:
        """ Save the new URL in the cache"""
        await Cache.set(url.short_id, url.url)
