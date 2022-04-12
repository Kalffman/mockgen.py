import abc

from domain.model.entity import PersonName, PersonFullName, PersonDocument
from domain.ports.output.data_access import PersonNameDataAccessPort, PersonDocumentDataAccessPort


class ConsultPersonNameUseCase(abc.ABC):

    person_name_data_access: PersonNameDataAccessPort

    @abc.abstractmethod
    def get_random_person_name(self) -> PersonName:
        raise NotImplementedError

    @abc.abstractmethod
    def get_random_full_name(self, weight: int) -> PersonFullName:
        raise NotImplementedError


class ConsultPersonDocumentUseCase(abc.ABC):

    person_document_data_access: PersonDocumentDataAccessPort

    @abc.abstractmethod
    def get_random_document(self) -> PersonDocument:
        raise NotImplementedError

