import requests
from common.logger_initializer import LOGGER
from common.configuration import CONF, ENUM
from common.utils import remove_double_spaces_from_string, remove_items_from_string

MORPHOLOGY_ANALYZE_URL = CONF['hebrew-nlp']['morphNormalize']

class nlp_hebrew_service(object):

    def __init__(self):
        pass

    def nlp_hebrew_call(self, doc: str, path: str):  
        request = {
        'token': CONF["hebrew-nlp"]["token"],
        "type": "SEARCH",                      
        "text": doc,
        }  
        result = None
        try: 
            result = requests.post(f'{CONF["hebrew-nlp"]["baseUrl"]}{path}', json=request).json()
            LOGGER.info('Created a NLP-hebrew call')
        except:
            result = None
            LOGGER.info("There was a problem with hebrew_nlp")
        return result
    
    def clean_hebrew_nlp_result(self, nlp_result):
        paragraph = ""
        for sentence in nlp_result:
            for word in sentence:
                if word in ENUM["irrelevant_part_of_speach"]:
                    LOGGER.info(f"Found a bad word")
                else:
                    paragraph += word + ' '
            paragraph += '\n'
        paragraph = remove_double_spaces_from_string(paragraph)
        return paragraph