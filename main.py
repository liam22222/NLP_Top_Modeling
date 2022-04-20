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

MONGO_DB = mongoDB_service()
NLP = nlp_hebrew_service()

coll_name = "raw_elstic"

# init_raw_data_from_elastic(coll_name)

# Normelize data
insert_normalized_collection(
   coll_name,
   "body",
   NLP,
   MONGO_DB)

def EylamsCsv(numberOfWordsInExpression: int ,collection_name: str, NLP: nlp_hebrew_service, MONGO_DB: mongoDB_service) -> None:
        tested_collection = MONGO_DB.get_collection(collection_name)
        final_csv = csv_handler("final")
        print(tested_collection)
        dictionary_of_the_csv={}
        all_words_set = set()
        list_of_rows_for_csv = []
        for doc in tested_collection.find():
            word_dict= n_words_frequency(doc['body'],numberOfWordsInExpression)
            all_words_set.update(word_dict.keys())
            dictionary_of_the_csv.update({doc["title"]:word_dict})
        for word in all_words_set:
            specific_row=[word]
            for key, value in dictionary_of_the_csv.items():
                if word in value:
                    specific_row.append(f"{key} : {value[word]}")
            list_of_rows_for_csv.append(specific_row)
        final_csv.write(list_of_rows_for_csv)



EylamsCsv(numberOfWordsInExpression = 3,
 collection_name ='normalized_raw_elstic',
 NLP = NLP,
 MONGO_DB = MONGO_DB)

# def sports(collection_name: str, NLP: nlp_hebrew_service, MONGO_DB: mongoDB_service) ->None:

