import pymongo
from common.logger_initializer import LOGGER
from common.configuration import CONF

class mongoDB_service(object):

    def __init__(self) -> None:
        self.__mongodb = pymongo.MongoClient(CONF['mongo']['url'])
        self.__dbCollection = self.__mongodb[CONF['mongo']['dbName']]
        
        
    def insert_one_object(self, col_name ,object ):
        db_col = self.__dbCollection[f"{col_name}"]
        db_col.insert_one(object)
        LOGGER.info('insert object '+ f"{object}" + ' to collection '+ col_name)
