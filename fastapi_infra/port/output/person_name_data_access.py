import csv
import random

from domain.ports.usecase.person_name_usecase import PersonNameDataAccessUseCase
from fastapi_infra.port.output.dto import PersonNameCSV
from fastapi_infra.port.output.person_name_data import PersonNameDataCSV


class PersonNameDataAccessCSV(PersonNameDataAccessUseCase):

    person_data = PersonNameDataCSV()

    async def get_random_person_name(self) -> PersonNameCSV:
        data = await self.person_data.get_data()

        s_random = random.SystemRandom()

        return s_random.choice(data)
