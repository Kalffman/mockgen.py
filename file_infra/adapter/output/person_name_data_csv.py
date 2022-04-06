import csv
import os

from domain.ports.usecase.person_name_usecase import PersonNameDataUseCase
from .model import PersonNameCSV


CSV_DATA_PATH = os.environ.get("NAME_DATA")


class PersonNameDataCSV(PersonNameDataUseCase):

    __person_names: list[PersonNameCSV]

    def __init__(self) -> None:
        self.__person_names = []

        with open(CSV_DATA_PATH, mode='r', encoding='UTF-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["alternative_names"] = row["alternative_names"].split('|')

                self.__person_names.append(PersonNameCSV(**row))

    async def get_data(self) -> list[PersonNameCSV]:
        return self.__person_names

