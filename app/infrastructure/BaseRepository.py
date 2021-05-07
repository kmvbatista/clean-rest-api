from typing import Generic, TypeVar, List
from app.extensions import mongo
from .BaseEntity import BaseEntity
from bson.json_util import dumps
from bson.objectid import ObjectId

BaseType = TypeVar(BaseEntity)

class BaseRepository(Generic[BaseType]):
    def __init__(self, table_name):
        self.table_name=table_name
        self.table = mongo.db[self.table_name]

    def get_all(self) -> List[BaseType]:
        all = self.table.find()
        return dumps(all)

    def get_by_id(self, id) -> BaseType:
        entity = self.table[self.table_name].find_one(
            {'_id':ObjectId(id)})
        return dumps(entity)

    def insert_one(self, entity: BaseType) -> None:
        self.table.insert(entity)

    def delete_one(self) -> None:
        self.table.delete_one({'_id': ObjectId(id)})

    def update(self, id, updated_entity) -> None:
        self.table.update_one({'_id': ObjectId(id)}, updated_entity)