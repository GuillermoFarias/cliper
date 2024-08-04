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

    async def create(self, model: GeneralStatistics) -> GeneralStatistics:
        """ Create a new model """
        repository = MongoDBRepository(self.connector, GeneralStatistics, 'statistics')
        return await repository.create(model)

    async def get_current(self) -> GeneralStatistics:
        """ Find a model by name """
        repository = MongoDBRepository(self.connector, GeneralStatistics, 'statistics')
        return await repository.find_one({'name': STATISTICS_NAME})

    async def create_index(self) -> None:
        """ Create indexes """
        repository = MongoDBRepository(self.connector, GeneralStatistics, 'statistics')
        await repository.create_index('short_id')

    async def update(self, model: GeneralStatistics) -> GeneralStatistics:
        """ Update a model """
        repository = MongoDBRepository(self.connector, GeneralStatistics, 'statistics')
        return await repository.update(model.id, model)
