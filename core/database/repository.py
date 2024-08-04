""" Repository pattern for MongoDB. """
from typing import Type
from bson import ObjectId
from pydantic import BaseModel
from core.database.connector import MongoDBConnector


class MongoDBRepository:
    """ A MongoDB repository class that handles CRUD operations. """

    def __init__(self, connector: MongoDBConnector, model: Type[BaseModel], collection_name: str):
        self.connector = connector
        self.model = model
        self.collection = connector.get_collection(collection_name)

    async def create(self, model: BaseModel) -> BaseModel:
        """Insert a new document into the collection."""
        model_dump = model.model_dump(by_alias=True)
        # remove id field from model_dump
        model_dump.pop('id', None)
        result = await self.collection.insert_one(model_dump)
        model.id = str(result.inserted_id)
        return model

    async def read(self, _id: str) -> BaseModel:
        """Retrieve a document by its ID."""
        document = await self.collection.find_one({"_id": ObjectId(_id)})
        if document:
            model = self.model.model_validate(document)
            model.id = str(document['_id'])
            return model
        return None

    async def update(self, _id: str, data: BaseModel):
        """Update an existing document."""
        model_dump = data.model_dump(by_alias=True)
        # remove id field from model_dump
        model_dump.pop('id', None)
        await self.collection.update_one({"_id": ObjectId(_id)}, {"$set": model_dump})

    async def update_many(self, query: dict, data: BaseModel):
        """Update multiple documents that match a query."""
        model_dump = data.model_dump(by_alias=True)
        # remove id field from model_dump
        model_dump.pop('id', None)
        await self.collection.update_many(query, {"$set": model_dump})

    async def delete(self, _id: str):
        """Delete a document by its ID."""
        await self.collection.delete_one({"_id": ObjectId(_id)})

    async def find(self, query: dict) -> list:
        """Find documents that match a query."""
        documents = self.collection.find(query)
        models = []
        async for document in documents:
            model = self.model.model_validate(document)
            model.id = str(document['_id'])
            models.append(model)

        return models

    async def find_one(self, query: dict) -> BaseModel:
        """Find a single document that matches a query."""
        document = await self.collection.find_one(query)
        if document:
            model = self.model.model_validate(document)
            model.id = str(document['_id'])
            return model
        return None

    async def count(self, query: dict) -> int:
        """Count documents that match a query."""
        return await self.collection.count_documents(query)

    async def drop(self):
        """Drop the collection."""
        await self.collection.drop()

    async def create_index(self, field: str | list):
        """Create an index on a field of the collection."""
        try:
            if isinstance(field, str):
                result = await self.collection.create_index([(field, 1)])
            if isinstance(field, list):
                result = await self.collection.create_index([(field, 1) for field in field])
            print(f"Index created: {result}")
        except Exception as e:
            print(f"Error creating index: {e}")