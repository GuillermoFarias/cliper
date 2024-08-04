"""General Statistics by url"""
from typing import Dict
from datetime import datetime
from pydantic import BaseModel, Field
from core.database.model import BaseModelWithId

STATISTICS_NAME = 'general_statistics_by_url'


class GeneralStatisticsByUrlData(BaseModel):
    """ General Statistics Data """
    total_access: int = 0
    total_access_by_country: Dict[str, int] = {}
    total_access_by_city: Dict[str, int] = {}
    total_access_by_device: Dict[str, int] = {}
    total_access_by_browser: Dict[str, int] = {}
    total_access_by_platform: Dict[str, int] = {}
    total_access_by_hour: Dict[str, int] = Field(default_factory=dict)


class GeneralStatisticsByUrl(BaseModelWithId):
    """ General Statistics """
    name: str
    url_id: str
    data: GeneralStatisticsByUrlData
    updated_at: datetime = Field(default_factory=datetime.now)
