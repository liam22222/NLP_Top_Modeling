from services.elastic_service import elasticsearch_service
from services.mongo_service import mongoDB_service
from services.html_parser_service import *

from common.configuration import CONF, ENUM


def init_raw_data_from_elastic(collection_name : str):
    elastic = elasticsearch_service()
    mongo = mongoDB_service()

    data = elastic.get_data_from_elastic(
        CONF["elasticsearch"]["url"],
        CONF["elasticsearch"]["userName"],
        CONF["elasticsearch"]["password"]
    )

    for document in data:
        html = document['_source']['text']
        
        checkURL = [x for x in ENUM["irrelevantSitesNames"] if (x in document['_source']['url'])]
        checkTitle = (document['_source']['title'] != "")

        abstract = find_abstract(html)
        body = find_body(html)
        summary = find_summary(html)

        if not checkURL and checkTitle and abstract and summary and body:
            mongo.insert_one_object(
                collection_name,
                {
                        "id": document['_id'],
                        "title": document['_source']['title'],
                        "url": document['_source']['url'],
                        "date": document['_source']['date'],
                        "abstract": abstract,
                        "body": body,
                        "summary": summary}
            )
