import random

from domain.ports.input.usecase import PersonNameDataAccessPort
from file_infra.adapter.output.model import PersonNameCSV
from file_infra.adapter.output.csv import PersonNameDataCSV


class PersonNameDataAccessCSV(PersonNameDataAccessPort):

    person_data = PersonNameDataCSV()

    async def get_random_name(self) -> PersonNameCSV:
        data = await self.person_data.get_data()

        s_random = random.SystemRandom()

        return s_random.choice(data)
