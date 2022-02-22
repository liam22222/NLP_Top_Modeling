import json
import requests
from requests.auth import HTTPBasicAuth
from NLP_Top_Modeling.common.logger_initializer import LOGGER
from NLP_Top_Modeling.common.configuration import CONF, ENUM


class elasticsearch_service(object):

    def __get_json(self, url: str, user: str, password: str):
        response = requests.get(
            f'{url}', auth=HTTPBasicAuth(f'{user}', f'{password}'))
       
        LOGGER.info('get data from elasticsearch')

        return json.dumps(response.json(), indent=4, sort_keys=True, ensure_ascii=False)

    def get_data_from_elastic(self, url: str, user: str, password: str):
        data = elasticsearch_service.__get_json(self, url, user, password)
        data = json.loads(data)
        data = data['hits']['hits']
        return data
