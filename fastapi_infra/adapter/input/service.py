from domain.model.entity import PersonName, PersonFullName
from domain.ports.input.usecase import ConsultPersonNameUseCase
from csv_file_infra.adapter.output.data_access import PersonNameDataAccessCSV


class PersonNameService(ConsultPersonNameUseCase):

    person_name_data_access = PersonNameDataAccessCSV()

    async def get_random_person_name(self) -> PersonName:
        person = await self.person_name_data_access.get_random_name()

        return person.to_model()

    async def get_random_full_name(self, weight: int) -> PersonFullName:
        full_name_arr = [await self.get_random_person_name() for _ in range(weight)]

        first_name = full_name_arr.pop(0)

        last_name = full_name_arr.pop(-1)

        middle_name = " ".join([p_name.random_variation() for p_name in full_name_arr])

        person_full_name = PersonFullName(
            first_name=first_name.name,
            last_name=last_name.name,
            full_name=f"{first_name.name} {middle_name} {last_name.name}"
        )

        return person_full_name
