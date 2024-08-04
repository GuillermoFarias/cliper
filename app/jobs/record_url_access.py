""" Save request of URL to make statistics """
import re
import geoip2.database
from user_agents import parse
from app.models.url import Url
from app.models.url_access_log import UrlAccessLog
from app.repositories.url_repository import UrlRepository
from app.repositories.url_access_log_repository import UrlAccessLogRepository
from app.jobs.update_general_stats import UpdateGeneralStats
from app.jobs.update_general_stats_by_url import UpdateGeneralStatsByUrl
from core.queue.contracts.job import Job
from core.support.inject import inject


class RecordUrlAccess(Job):
    """ Save request of URL to make statistics """

    @inject
    def __init__(self, url_repository: UrlRepository, url_access_log_repository: UrlAccessLogRepository):
        """ Constructor """
        self.url_repository = url_repository
        self.url_access_log_repository = url_access_log_repository

    async def handle(self, data: dict) -> bool:
        """ Handle the process """
        request = data.get('request')
        short_id = data.get('short_id')
        response_time = data.get('response_time')
        url: Url = await self.url_repository.find_by_short_id(short_id)

        ip = request.get('ip', 'Unknown')
        user_agent = request.get('user_agent', 'Unknown')
        referer = request.get('referer', 'Unknown')

        if re.match(r'^192\.168\.', ip):
            country = "Local"
            city = "Local"
        else:
            try:
                reader = geoip2.database.Reader('/app/storage/GeoIP/GeoLite2-City.mmdb')
                response = reader.city(ip)
                country = response.country.iso_code
                city = response.city.name
            except geoip2.errors.AddressNotFoundError:
                country = "Unknown"
                city = "Unknown"

        device = self.get_device_from_user_agent(user_agent)
        browser = self.get_browser_from_user_agent(user_agent)
        platform = self.get_platform_from_user_agent(user_agent)

        access_entry = UrlAccessLog(
            url_id=url.id,
            ip=ip,
            device=device,
            browser=browser,
            platform=platform,
            referer=referer,
            user_agent=user_agent,
            country=country,
            city=city,
            response_time=response_time
        )

        access_entry = await self.url_access_log_repository.create(access_entry)
        await UpdateGeneralStats.dispatch_async({'access_log_id': access_entry.id})
        await UpdateGeneralStatsByUrl.dispatch_async({'access_log_id': access_entry.id, 'url_id': url.id})

    def get_device_from_user_agent(self, user_agent: str) -> str:
        """ Get device from user agent """
        user_agent_obj = parse(user_agent)
        if user_agent_obj.is_mobile:
            return "Mobile"
        elif user_agent_obj.is_tablet:
            return "Tablet"
        elif user_agent_obj.is_pc:
            return "Desktop"
        else:
            return "Unknown"

    def get_browser_from_user_agent(self, user_agent: str) -> str:
        """ Get browser from user agent """
        user_agent_obj = parse(user_agent)
        browser = user_agent_obj.browser.family
        version = user_agent_obj.browser.version_string
        return f"{browser} {version}"

    def get_platform_from_user_agent(self, user_agent: str) -> str:
        """ Get platform from user agent """
        user_agent_obj = parse(user_agent)
        os = user_agent_obj.os.family
        version = user_agent_obj.os.version_string
        return f"{os} {version}"
