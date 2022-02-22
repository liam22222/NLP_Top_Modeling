from logging import exception
from bson.objectid import ObjectId
import pymongo
from pymongo import collection
from NLP_Top_Modeling.common.logger_initializer import LOGGER
from NLP_Top_Modeling.common.configuration import CONF
import numbers
import numpy as np

class mongoDB_service(object):

    def __init__(self) -> None:
        self.mongodb = pymongo.MongoClient(CONF['mongo']['url'])
        self.dbName = self.mongodb[CONF['mongo']['dbName']]

    def get_collection(self, collection_name: str):
        return self.dbName[f"{collection_name}"]

    def get_document_by_id(self, collection_name: str ,document_id: str):
        return self.dbName[f"{collection_name}"].find_one({'_id': ObjectId(document_id)})

    def insert_one_object(self, col_name, doc):
        db_col = self.dbName[f"{col_name}"]
        db_col.insert_one(doc)
        LOGGER.info('insert object ' + f"{doc}" + ' to collection ' + col_name)

    def insert_many_docs(self, collection_name, docs_as_list):
        db_col = self.dbName[f"{collection_name}"]
        db_col.insert_many(docs_as_list)
        LOGGER.info(f'Insert to collection {collection_name}, documents')

    def delete_one_object(self, col_name, doc):
        db_col = self.dbName[f"{col_name}"]
        db_col.delete_one(doc)
        LOGGER.info('delete object ' + f"{doc}" + ' to collection ' + col_name)

    def delete_many_object(self, col_name, doc):
        db_col = self.dbName[f"{col_name}"]
        db_col.delete_many(doc)
        LOGGER.info('Delete %from collection ' + f"{doc}" + ' to collection ' + col_name)

    def count_diffrent_rows(self, collection_name, rowA: str, rowB: str):
        """
        Parameters
        ----------
        collection_name - collection name of mongoDB
        rowA - row A we want to check
        rowB - row B we want to check

        Returns
        -------
        returns a true if number of row A equals to row B
        """
        db_col = self.dbName[f"{collection_name}"]
        counter = 0
        for doc in db_col.find():
            if doc[rowA] != None and doc[rowB] != None:
                counter += 1
        print(counter)
        if counter == 0:
            return False
        return True

    def outlier_detection_iqr(self, list: list):
        help_list = []
        for ele in list:
            Q1 = np.percentile(list, 25)
            Q3 = np.percentile(list, 75)
            IQR = Q3 - Q1
            IQR_range = IQR * 1.5
            if (ele < Q1 - IQR_range) or (ele > Q3 + IQR_range):
                print(ele)
                ele = np.nan
            help_list.append(ele)
        print(help_list)
        return help_list

    def check_words_amount(self, collection_name):
        db_col = self.dbName[f"{collection_name}"]
        list = []
        for doc in db_col.find():
            list.append(len(doc['text'].split()))
        print(list)
        procssed_list_iqr = self.outlier_detection_iqr(list)
        return procssed_list_iqr