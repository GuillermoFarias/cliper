""" Save request of URL to make statistics """
from app.models.url_access_log import UrlAccessLog
from app.models.general_statistics import GeneralStatisticsData
from app.models.general_statistics import GeneralStatistics
from app.repositories.general_statistics_repository import GeneralStatisticsRepository
from app.repositories.url_access_log_repository import UrlAccessLogRepository
from core.queue.contracts.job import Job
from core.support.inject import inject


class UpdateGeneralStats(Job):
    """ Save request of URL to make statistics """

    @inject
    def __init__(self,
                 statistics_repository: GeneralStatisticsRepository,
                 url_access_log_repository: UrlAccessLogRepository
                 ):
        """ Constructor """
        self.statistics_repository = statistics_repository
        self.url_access_log_repository = url_access_log_repository

    async def handle(self, data: dict) -> bool:
        """ Handle the process """
        access_log_id = data.get('access_log_id')
        log: UrlAccessLog = await self.url_access_log_repository.find_by_id(access_log_id)
        current_stats: GeneralStatistics = await self.statistics_repository.get_current()

        if current_stats:
            current_stats_data = current_stats.data
            current_stats_data.total_access += 1

            if log.country in current_stats_data.total_access_by_country:
                current_stats_data.total_access_by_country[log.country] += 1
            else:
                current_stats_data.total_access_by_country[log.country] = 1

            if log.city in current_stats_data.total_access_by_city:
                current_stats_data.total_access_by_city[log.city] += 1
            else:
                current_stats_data.total_access_by_city[log.city] = 1

            if log.device in current_stats_data.total_access_by_device:
                current_stats_data.total_access_by_device[log.device] += 1
            else:
                current_stats_data.total_access_by_device[log.device] = 1

            if log.browser in current_stats_data.total_access_by_browser:
                current_stats_data.total_access_by_browser[log.browser] += 1
            else:
                current_stats_data.total_access_by_browser[log.browser] = 1

            if log.platform in current_stats_data.total_access_by_platform:
                current_stats_data.total_access_by_platform[log.platform] += 1
            else:
                current_stats_data.total_access_by_platform[log.platform] = 1

            if log.timestamp.hour in current_stats_data.total_access_by_hour:
                current_stats_data.total_access_by_hour[str(log.timestamp.hour)] += 1
            else:
                current_stats_data.total_access_by_hour[str(log.timestamp.hour)] = 1

            current_stats.data = current_stats_data
            await self.statistics_repository.update(current_stats)
        else:
            new_stats_data = GeneralStatisticsData(
                total_access=1,
                total_access_by_country={log.country: 1},
                total_access_by_city={log.city: 1},
                total_access_by_device={log.device: 1},
                total_access_by_browser={log.browser: 1},
                total_access_by_platform={log.platform: 1},
                total_access_by_hour={str(log.timestamp.hour): 1},
            )

            new_stats = GeneralStatistics(
                name='general_statistics',
                data=new_stats_data
            )

            await self.statistics_repository.create(new_stats)

        return True
