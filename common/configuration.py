import json
import logging
import os

from common.logger_initializer import LOGGER
from common.utils import wrap_exception


CURR_PATH = os.path.abspath(os.path.dirname(__file__))
JSON_CONF_FILENAME = LOGGING_FILE_DIRECTORY = os.path.join(CURR_PATH, "../resources/config.json")
JSON_ENUM_FILENAME = LOGGING_FILE_DIRECTORY = os.path.join(CURR_PATH, "../resources/enums.json")


def load_configuration() -> dict:
    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        config_path = os.path.join(my_path, JSON_CONF_FILENAME)
        with open(config_path, 'r') as f:
            conf = json.load(f)
            for key, value in conf.items():
                LOGGER.info(f"Loaded the '{key}' key with the '{value}' value")
            return conf
    except (OSError, ValueError) as e:
        logging.error(wrap_exception(e, "Could not load the configuration"))

def load_enums() -> dict:
    try:
        my_path = os.path.abspath(os.path.dirname(__file__))
        config_path = os.path.join(my_path, JSON_ENUM_FILENAME)
        with open(config_path, 'r') as f:
            enum = json.load(f)
            for key, value in enum.items():
                LOGGER.info(f"Loaded the '{key}' key with the '{value}' value")
            return enum
    except (OSError, ValueError) as e:
        logging.error(wrap_exception(e, "Could not load the enums"))


CONF = load_configuration()
ENUM = load_enums()