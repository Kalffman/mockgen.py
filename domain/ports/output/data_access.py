import abc

from domain.ports.output.model import Data


class ResourceData(abc.ABC):

    @abc.abstractmethod
    async def get_data(self) -> any:
        raise NotImplementedError


class PersonNameDataAccessPort(abc.ABC):

    person_data: ResourceData

    @abc.abstractmethod
    async def get_random_name(self) -> Data:
        raise NotImplementedError


class PersonDocumentDataAccessPort(abc.ABC):

    document_data: ResourceData

    @abc.abstractmethod
    async def get_random_document(self) -> Data:
        raise NotImplementedError
