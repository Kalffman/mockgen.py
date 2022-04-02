from domain.model.entity import PersonName
from domain.ports.usecase.person_name_usecase import ConsultPersonNameUseCase
from fastapi_infra.port.output.person_name_data_access import PersonNameDataAccessCSV


class PersonNameService(ConsultPersonNameUseCase):

    __person_name_data_access = PersonNameDataAccessCSV()

    async def get_random_person_name(self) -> PersonName:
        person = await self.__person_name_data_access.get_random_person_name()

        return PersonName(
            name=person.group_name,
            variations=person.alternative_names
        )
