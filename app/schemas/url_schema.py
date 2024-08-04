""" Url schema for pydantic validation """
from pydantic import BaseModel


class URLCreate(BaseModel):
    """ URL Create Schema """
    url: str


class URLResponse(BaseModel):
    """ URL Response Schema """
    short_id: str
    url: str
