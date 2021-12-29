from os import listxattr
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
        self.writer = csv.writer(self.file)

    async def __write_single_row(self, rowToWrite: list) -> None:
        """This function writes and log what ever you want to write"""
        try:
            self.writer.writerow(rowToWrite)
            LOGGER.info(f"Wrote new line into {self.file_path}")
        except:
            LOGGER.info(f"Couldent write new line into {self.file_path}")
        
    async def __write_rows_to_csv(self, rows: list) -> None:
        """This function Writes in async way your rows.\n Rows are list of lists that each list is an row to write"""
        await asyncio.gather(*[self.__write_single_row(row) for row in rows])

    def write(self, rows: list) -> None:
        """
        The function gets list of rows (Each row is a list) and write it
        Rows for example : [["Name", "age", "gender"], ["Liam", "21", "M"], ["Ron", "26", "M"]]
        """
        asyncio.run(self.__write_rows_to_csv(rows))