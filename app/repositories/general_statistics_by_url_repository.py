""" Statistics by url Repository """
from app.models.general_statistics_url import GeneralStatisticsByUrl
from app.models.general_statistics_url import STATISTICS_NAME
from core.database.repository import MongoDBRepository
from core.database.connector import MongoDBConnector


class GeneralStatisticsByUrlRepository:
    """ Statistics by url Repository """

    def __init__(self, connector: MongoDBConnector):
        """ Constructor """
        self.connector = connector

    async def create(self, model: GeneralStatisticsByUrl) -> GeneralStatisticsByUrl:
        """ Create a new model """
        repository = MongoDBRepository(self.connector, GeneralStatisticsByUrl, 'statistics')
        return await repository.create(model)

    async def get_by_url_id(self, url_id: str) -> GeneralStatisticsByUrl:
        """ Find a model by name """
        repository = MongoDBRepository(self.connector, GeneralStatisticsByUrl, 'statistics')
        return await repository.find_one({'name': STATISTICS_NAME, 'url_id': url_id})

    async def update(self, model: GeneralStatisticsByUrl) -> GeneralStatisticsByUrl:
        """ Update a model """
        repository = MongoDBRepository(self.connector, GeneralStatisticsByUrl, 'statistics')
        return await repository.update(model.id, model)