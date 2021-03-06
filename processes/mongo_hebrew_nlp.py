from services.nlp_hebrew_service import nlp_hebrew_service
from services.mongo_service import mongoDB_service
from common.utils import remove_items_from_string

from common.logger_initializer import LOGGER
from common.configuration import CONF, ENUM

def normelize_collection(collection, field_to_normalize: str, NLP: nlp_hebrew_service):
    docs_as_list = []
    for doc in collection.find():
        text =doc[f"{field_to_normalize}"]
        hebrew_result = NLP.nlp_hebrew_call(text, CONF["hebrew-nlp"]["morphNormalize"])
        if hebrew_result == None:
            continue                                                                 
        paragraph = NLP.clean_hebrew_nlp_result(hebrew_result)
        doc[f"{field_to_normalize}"] = remove_items_from_string(paragraph, ENUM["irrelevant_signs"])
        docs_as_list.append(doc)

    LOGGER.info(f"We just normalize {field_to_normalize}")
    return docs_as_list
            

def insert_normalized_collection(collection_name: str, field_to_normalize: str, NLP: nlp_hebrew_service, MONGO_DB: mongoDB_service):
    """
    This function normalize any field you want to by the following assumptions:\n
    collection_name = The name of the collection you want to normalize from the mongoDB\n
    field_to_normalize = Which field from the documents in the collection you wish to normalize\n
    NLP = Global instance of NLP_hebrew\n
    MONGO_DB = Global instance of Mongo db
    """
    raw_collection = MONGO_DB.get_collection(collection_name)
    norm_coll_list = normelize_collection(raw_collection, field_to_normalize, NLP)
    MONGO_DB.insert_many_docs(f"normalized_{collection_name}", norm_coll_list)