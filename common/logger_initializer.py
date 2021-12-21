import logging
import os

from logging.handlers import TimedRotatingFileHandler


CURR_PATH = os.path.abspath(os.path.dirname(__file__))
LOGGING_FILE_DIRECTORY = os.path.join(CURR_PATH, "../../data/logs")
LOGGING_FILE_PATH = os.path.join(LOGGING_FILE_DIRECTORY, "application.log")
LOGGING_FORMAT = "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
LOGGING_LEVEL = "INFO"
LOGGING_WHEN = "midnight"
LOGGING_INTERVAL = 1


def create_logs_directory() -> None:
    if not os.path.exists(LOGGING_FILE_DIRECTORY):
        os.makedirs(LOGGING_FILE_DIRECTORY)


def init_logger():
    """ Initialize the logger with StreamHandler and TimedRotatingFileHandler """
    inner_logger = logging.getLogger(__name__)
    inner_logger.setLevel(LOGGING_LEVEL)
    stream_handler = logging.StreamHandler()
    file_rotating_handler = TimedRotatingFileHandler(LOGGING_FILE_PATH, when=LOGGING_WHEN, interval=LOGGING_INTERVAL)
    stream_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    file_rotating_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    inner_logger.addHandler(stream_handler)
    inner_logger.addHandler(file_rotating_handler)
    inner_logger.info("Finished initializing the logger of the project")
    return inner_logger


create_logs_directory()
LOGGER = init_logger()
