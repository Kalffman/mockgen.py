import random

from domain.ports.usecase.person_name_usecase import PersonNameDataAccessUseCase
from file_infra.adapter.output.model import PersonNameCSV
from file_infra.adapter.output.person_name_data_csv import PersonNameDataCSV


class PersonNameDataAccessCSV(PersonNameDataAccessUseCase):

    person_data = PersonNameDataCSV()

    async def get_random_name(self) -> PersonNameCSV:
        data = await self.person_data.get_data()

        s_random = random.SystemRandom()

        return s_random.choice(data)
