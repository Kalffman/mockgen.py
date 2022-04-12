from domain.model.entity import Data
from domain.ports.output.data_access import PersonDocumentDataAccessPort
from random import randint


class CPFDataAccessGenerator(PersonDocumentDataAccessPort):

    async def get_random_document(self) -> Data:
        one = 0
        two = 0
        three = 0
