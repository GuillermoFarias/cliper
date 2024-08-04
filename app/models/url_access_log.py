""" Url Access Log Model"""

from datetime import datetime
from pydantic import Field
from core.database.model import BaseModelWithId


class UrlAccessLog(BaseModelWithId):
    """ Url Access Log Model """
    url_id: str
    ip: str
    device: str
    browser: str
    platform: str
    timestamp: datetime = Field(default_factory=datetime.now)
    referer: str = None  # Optional: Referer header
    user_agent: str = None  # Optional: Full User-Agent string
    response_time: float = None  # Optional: Response time in seconds
    country: str = None  # Optional: Country code
    city: str = None  # Optional: City name
