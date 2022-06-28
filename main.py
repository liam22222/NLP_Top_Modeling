import csv
from typing import Set
import pymongo
from services.mongo_service import mongoDB_service
from services.nlp_hebrew_service import nlp_hebrew_service
from services.csv import csv_handler
from common.logger_initializer import LOGGER
from common.utils import *
from requests.auth import HTTPBasicAuth
import json
from processes.EDA import n_words_frequency
from processes.elastic_to_mogno import init_raw_data_from_elastic
from processes.mongo_hebrew_nlp import insert_normalized_collection
from common.configuration import CONF, ENUM
from modelling.LDA_train import lda_train
from processes.mongo_to_list import mongo_to_list

MONGO_DB = mongoDB_service()
NLP = nlp_hebrew_service()

coll_name = "raw_elstic"

init_raw_data_from_elastic(coll_name)

# Normelize data
insert_normalized_collection(
   coll_name,
   "body",
   NLP,
   MONGO_DB)

# Prepare for modelling
normalized_data = mongo_to_list("raw_elstic")
normalized_body_list = get_body_list(normalized_data)

