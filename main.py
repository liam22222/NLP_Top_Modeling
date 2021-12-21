import json
import pymongo
import requests
from common.utils import *

from requests.auth import HTTPBasicAuth
from common.configuration import CONF


# projectName = conf['mongo']['dbName']
# myClient = pymongo.MongoClient(conf['mongo']['url'])
# dbName = myClient[projectName]
# mycol = dbName["raw_elasticsearch"]

from services.mongo_service import mongoDB_service

m = mongoDB_service()
m.insert_one_object('bla',{'ron': 'ron'})

