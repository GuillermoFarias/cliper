""" Statistics Repository """
from app.models.general_statistics import GeneralStatistics
from app.models.general_statistics import STATISTICS_NAME
from core.database.repository import MongoDBRepository
from core.database.connector import MongoDBConnector


class GeneralStatisticsRepository:
    """ Statistics Repository """

    def __init__(self, connector: MongoDBConnector):
        """ Constructor """
        self.connector = connector
        self.repository = MongoDBRepository(self.connector, GeneralStatistics, 'statistics')

    async def create(self, model: GeneralStatistics) -> GeneralStatistics:
        """ Create a new model """
        return await self.repository.create(model)

    async def get_current(self) -> GeneralStatistics:
        """ Find a model by name """
        return await self.repository.find_one({'name': STATISTICS_NAME})

    async def create_index(self) -> None:
        """ Create indexes """
        await self.repository.create_index('short_id')

    async def update(self, model: GeneralStatistics) -> GeneralStatistics:
        """ Update a model """
        return await self.repository.update(model.id, model)
