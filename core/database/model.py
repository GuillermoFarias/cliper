""" Base model for all models in the application. """
from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId


class BaseModelWithId(BaseModel):
    """ Base model for all models in the application. """
    id: Optional[str] = Field(default=None, alias='id')

    class Config:
        """ Pydantic configuration. """
        json_encoders = {
            ObjectId: str
        }
