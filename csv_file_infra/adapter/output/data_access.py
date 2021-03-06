import csv
import os
import random

from domain.ports.output.data_access import PersonNameDataAccessPort, ResourceData
from .model import PersonNameCSV


CSV_PERSON_NAME_DATA_PATH = os.environ.get("PERSON_NAME_DATA")


class PersonNameDataAccessCSV(PersonNameDataAccessPort):

    class PersonNameDataCSV(ResourceData):
        __person_names: list[PersonNameCSV]

        def __init__(self) -> None:
            self.__person_names = []

            with open(CSV_PERSON_NAME_DATA_PATH, mode='r', encoding='UTF-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    row["alternative_names"] = row["alternative_names"].split('|')

                    self.__person_names.append(PersonNameCSV(**row))

        async def get_data(self) -> list[PersonNameCSV]:
            return self.__person_names

    person_data = PersonNameDataCSV()

    async def get_random_name(self) -> PersonNameCSV:
        data = await self.person_data.get_data()

        s_random = random.SystemRandom()

        return s_random.choice(data)
