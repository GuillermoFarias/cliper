""" Class containing the API endpoints for the application. """
import time
import random
import string
from fastapi import Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import JSONResponse
from app.schemas.url_schema import URLCreate
from app.models.url import Url
from app.models.general_statistics import GeneralStatistics
from app.models.general_statistics_url import GeneralStatisticsByUrl
from app.jobs.create_new_url import CreateNewUrl
from app.jobs.record_url_access import RecordUrlAccess
from app.repositories.url_repository import UrlRepository
from app.repositories.general_statistics_repository import GeneralStatisticsRepository
from app.repositories.general_statistics_by_url_repository import GeneralStatisticsByUrlRepository
from core.facades.env import get_app_url
from core.facades.cache import Cache
from core.support.inject import inject


class ApiController:
    """ Controller for the API. """

    @inject
    def __init__(self,
                 url_repository: UrlRepository,
                 stats_repository: GeneralStatisticsRepository,
                 stats_by_url_repository: GeneralStatisticsByUrlRepository
                 ):
        """ Constructor """
        self.url_repository = url_repository
        self.stats_repository = stats_repository
        self.stats_by_url_repository = stats_by_url_repository

    async def ping(self, request: Request):
        """ Ping route for the API. """
        return {'data': 'pong'}

    async def create_url(self, request: Request, url: URLCreate):
        """ Index route for the API. """
        base_url = get_app_url()
        short_url_id = self.get_short_id()
        await CreateNewUrl.dispatch_async({'url': url.url, 'short_id': short_url_id})
        return {'url': url.url, 'short_url': f'{base_url}/{short_url_id}'}

    def get_short_id(self) -> str:
        """ Get new short URL ID """
        length = 8
        return ''.join(random.choices(string.ascii_letters, k=length))

    async def get_url(self, request: Request, short_url: str):
        """ Get URL by short URL """
        url: Url = await self.url_repository.find_by_short_id(short_url)
        if url is None:
            raise HTTPException(status_code=404, detail="URL not found")

        return {'data': url}

    async def redirect_url(self, request: Request, short_url: str):
        """ Redirect to URL """
        start_time = time.time()
        original_url = await Cache.get(short_url)
        if not original_url:
            url: Url = await self.url_repository.find_by_short_id(short_url)
            if url is None:
                raise HTTPException(status_code=404, detail="URL not found")
            original_url = url.url
            await Cache.set(short_url, original_url)

        response = RedirectResponse(url=original_url, status_code=307)
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Expires'] = '0'

        request_data = {
            'short_id': original_url,
            'response_time': time.time() - start_time,
            'ip': request.client.host,
            'user_agent': request.headers.get('User-Agent', 'Unknown'),
            'referer': request.headers.get('Referer', 'Unknown'),
            'timestamp': time.time(),
        }

        await RecordUrlAccess.dispatch_async({
            'short_id': short_url,
            'request': request_data,
            'response_time': time.time() - start_time
        })

        return response

    async def delete_url(self, request: Request, short_url: str):
        """ Delete URL """
        url: Url = await self.url_repository.find_by_short_id(short_url)
        if not url:
            raise HTTPException(status_code=404, detail="URL not found")
        await self.url_repository.delete(url)
        await Cache.delete(short_url)

        return JSONResponse({"message": "URL deleted"}, status_code=204)

    async def get_url_stats(self, request: Request, short_url: str):
        """ Get URL stats """
        url: Url = await self.url_repository.find_by_short_id(short_url)
        if not url:
            raise HTTPException(status_code=404, detail="URL not found")

        general_stats: GeneralStatisticsByUrl = await self.stats_by_url_repository.get_by_url_id(url.id)
        if not general_stats:
            raise HTTPException(status_code=404, detail="URL stats not found")

        return {'data': general_stats.data}

    async def get_general_stats(self, request: Request):
        """ Get general stats """
        general_stats: GeneralStatistics = await self.stats_repository.get_current()

        return {'data': general_stats.data}
