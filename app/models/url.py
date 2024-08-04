""" Url Model"""

from datetime import datetime
from pydantic import Field
from core.database.model import BaseModelWithId


class Url(BaseModelWithId):
    """ Url Model """
    short_id: str
    url: str
    created_at: datetime = Field(default_factory=datetime.now)
