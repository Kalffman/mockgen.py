import abc

from domain.model.entity import Data


class PersonNameDataAccessPort(abc.ABC):

    class PersonNameData(abc.ABC):

        @abc.abstractmethod
        async def get_data(self) -> any:
            raise NotImplementedError

    person_data: PersonNameData

    @abc.abstractmethod
    async def get_random_name(self) -> Data:
        raise NotImplementedError


class PersonDocumentDataAccessPort(abc.ABC):

    class PersonDocumentData(abc.ABC):

        @abc.abstractmethod
        async def get_data(self) -> any:
            raise NotImplementedError

    document_data: PersonDocumentData

    @abc.abstractmethod
    async def get_random_document(self) -> Data:
        raise NotImplementedError
