import abc

from domain.ports.input.model import PersonName, PersonFullName, PersonDocument, Person
from domain.ports.output.data_access import PersonNameDataAccessPort, PersonDocumentDataAccessPort


class ConsultPersonNameUseCase(abc.ABC):

    person_name_data_access: PersonNameDataAccessPort

    @abc.abstractmethod
    async def get_random_person_name(self) -> PersonName:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_random_full_name(self, weight: int) -> PersonFullName:
        raise NotImplementedError


class ConsultPersonDocumentUseCase(abc.ABC):

    person_document_data_access: PersonDocumentDataAccessPort

    @abc.abstractmethod
    async def get_random_document(self, mask: bool) -> PersonDocument:
        raise NotImplementedError


class ConsultPersonUseCase(abc.ABC):

    person_name_use_case: ConsultPersonNameUseCase
    person_document_use_case: ConsultPersonDocumentUseCase

    async def get_random_person(self, mask: bool, weight: int) -> Person:
        full_name = await self.person_name_use_case.get_random_full_name(weight)
        document = await self.person_document_use_case.get_random_document(mask)

        return Person(
            name=full_name,
            documents=[document]
        )
