from common.logger_initializer import LOGGER
from common.configuration import CONF, ENUM
from pathlib import Path
import asyncio
import csv
import os

class csv_handler(object):
    
    def __init__(self, name: str) -> None:
        self.file_path = os.getcwd() + CONF["csv"]["path"] + name + ".csv"
        self.file = open(self.file_path, 'w')
        self.__writer = csv.writer(self.file)

    def write(self, rows: list) -> None:
        """
        The function gets list of rows (Each row is a list) and write it
        Rows for example : [["Name", "age", "gender"], ["Liam", "21", "M"], ["Ron", "26", "M"]]
        """
        self.__writer.writerows(rows)