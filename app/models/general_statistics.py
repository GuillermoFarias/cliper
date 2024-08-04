"""General Statistics"""
from typing import Dict
from datetime import datetime
from pydantic import BaseModel, Field
from core.database.model import BaseModelWithId

STATISTICS_NAME = 'general_statistics'


class GeneralStatisticsData(BaseModel):
    """ General Statistics Data """
    total_access: int = 0
    total_access_by_country: Dict[str, int] = {}
    total_access_by_city: Dict[str, int] = {}
    total_access_by_device: Dict[str, int] = {}
    total_access_by_browser: Dict[str, int] = {}
    total_access_by_platform: Dict[str, int] = {}
    total_access_by_hour: Dict[str, int] = Field(default_factory=dict)


class GeneralStatistics(BaseModelWithId):
    """ General Statistics """
    name: str
    data: GeneralStatisticsData
    updated_at: datetime = Field(default_factory=datetime.now)
