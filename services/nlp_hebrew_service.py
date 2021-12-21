import pymongo
import requests 

from common.logger_initializer import LOGGER
from common.configuration import conf

class nlp_hebrew_service(object):

    def normalize_by_irrelevant_parts_of_speach(self, dbcol):  
        # call monogo service  
        myclient = pymongo.MongoClient(conf['mongo']['url'])
        mydb = myclient[conf['dbName']]
        mycol = mydb[dbcol]

    

