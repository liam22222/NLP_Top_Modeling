import requests
from common.logger_initializer import LOGGER
from common.configuration import CONF, ENUM
from common.utils import remove_items_from_string

MORPHOLOGY_ANALYZE_URL = "/Morphology/Analyze"

class nlp_hebrew_service(object):

    def __init__(self):
        pass

    def nlp_hebrew_call(self, doc: str, path: str):  
        request = {
        'token': CONF["hebrew-nlp"]["token"],
        'readable': False,
        'paragraph':  doc,
        }  
        result = requests.post(f'{CONF["hebrew-nlp"]["baseUrl"]}{path}', json=request).json()
        LOGGER.info('Created a NLP-hebrew call')
        return result
    
    def clean_hebrew_nlp_result(self, nlp_result):
        paragraph = ""
        for sentence in nlp_result:
            for word in sentence:
                best_option = word[0]
                if best_option['partOfSpeech'] in ENUM["irrelevant_part_of_speach"]:
                    LOGGER.info(f"Found a bad word")
                else:
                    paragraph += best_option["baseWord"] + ' '
            paragraph += '\n'
        
        return paragraph