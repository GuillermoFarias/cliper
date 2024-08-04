""" App provider """
from app.repositories.url_repository import UrlRepository
from core.contracts.provider import Provider
from core.container import Container
from core.database.connector import MongoDBConnector


class AppProvider(Provider):
    """ Cache provider. """
