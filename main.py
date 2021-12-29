import pymongo
from services.mongo_service import mongoDB_service
from services.nlp_hebrew_service import nlp_hebrew_service
from services.csv import csv_handler
from common.logger_initializer import LOGGER
from common.utils import *
from requests.auth import HTTPBasicAuth


from processes.elastic_to_mogno import init_raw_data_from_elastic
from processes.mongo_hebrew_nlp import insert_normalized_collection
from common.configuration import CONF, ENUM

# MONGO_DB = mongoDB_service()
# NLP = nlp_hebrew_service()

# coll_name = "raw_elstic"

# # Init mongo from elastic
# init_raw_data_from_elastic(coll_name)

# # Normelize data
# insert_normalized_collection(
#    coll_name,
#    "body",
#    NLP,
#    MONGO_DB)
