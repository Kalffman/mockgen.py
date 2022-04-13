from algorithm_infra.adapter.output.data_access import CPFDataAccessGenerator
from domain.ports.input.model import PersonName, PersonFullName, PersonDocument
from domain.ports.input.usecase import ConsultPersonNameUseCase, ConsultPersonDocumentUseCase, ConsultPersonUseCase
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
            full_name=f"{first_name.name} {middle_name} {last_name.name}",
            gender=first_name.gender
        )

        return person_full_name


class CPFService(ConsultPersonDocumentUseCase):

    person_document_data_access = CPFDataAccessGenerator()

    async def get_random_document(self, mask: bool = False) -> PersonDocument:
        document = await self.person_document_data_access.get_random_document()

        if mask:
            document.cpf = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*document.cpf)

        return document.to_model()


class PersonService(ConsultPersonUseCase):
    person_name_use_case = PersonNameService()
    person_document_use_case = CPFService()
