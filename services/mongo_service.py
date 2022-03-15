from logging import exception
from bson.objectid import ObjectId
import pymongo
from pymongo import collection
from common.logger_initializer import LOGGER
from common.configuration import CONF

class mongoDB_service(object):

    def __init__(self) -> None:
        self.mongodb = pymongo.MongoClient(CONF['mongo']['url'])
        self.dbName = self.mongodb[CONF['mongo']['dbName']]
        
    def get_collection(self, collection_name: str):
        return self.dbName[f"{collection_name}"]

    def get_document_by_id(self, collection_name: str ,document_id: str):
        return self.dbName[f"{collection_name}"].find_one({'_id': ObjectId(document_id)})

    def insert_one_object(self, col_name ,object):
        db_col = self.dbName[f"{col_name}"]
        db_col.insert_one(object)
        LOGGER.info('insert object '+ f"{object}" + ' to collection '+ col_name)

    def insert_many_docs(self,collection_name,docs_as_list):
        db_col = self.dbName[f"{collection_name}"]
        db_col.insert_many(docs_as_list)
        LOGGER.info(f'Insert to collection {collection_name}, documents')

    def drop_collection(self, collection_name: str) -> None:
        my_collection = self.dbName[f"{collection_name}"]
        try:
            my_collection.drop()
            LOGGER.info(f"Dropped {collection_name}")
            
        except exception:
            LOGGER.info(f"Cant drop the {collection_name}, {exception}")