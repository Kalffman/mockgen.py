import abc

from types import MethodType
from domain.model.entity import PersonName


class PersonNameDataUseCase(abc.ABC):

    @abc.abstractmethod
    async def get_data(self) -> any:
        raise NotImplementedError


class PersonNameDataAccessUseCase(abc.ABC):
    person_data: PersonNameDataUseCase

    async def get_random_person_name(self) -> any:
        raise NotImplementedError


class ConsultPersonNameUseCase(abc.ABC):

    person_name_data_access: PersonNameDataAccessUseCase

    @abc.abstractmethod
    def get_random_person_name(self) -> PersonName:
        raise NotImplementedError
