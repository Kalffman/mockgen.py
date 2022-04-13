from algorithm_infra.adapter.output.model import CPF
from domain.ports.output.model import Data
from domain.ports.output.data_access import PersonDocumentDataAccessPort, ResourceData
from random import randint


class CPFDataAccessGenerator(PersonDocumentDataAccessPort):

    class CPFDocumentDataGen(ResourceData):

        @staticmethod
        def extract_verifier(numbers: dict):
            dv = 0

            for it in numbers.values():
                dv += it["mult"]

            dv = 11 - divmod(dv, 11)[1]

            return 0 if dv >= 10 else dv

        @staticmethod
        def multiply_factor(numbers: dict):
            numbers_len = len(numbers) + 1
            for idx, it in enumerate(numbers):
                fac = numbers_len - idx

                numbers[it]["mult"] = numbers[it]["origin"] * fac

            return numbers

        async def get_data(self) -> str:
            numbers = {
                "n1": {"origin": randint(0, 9), "mult": 0},
                "n2": {"origin": randint(0, 9), "mult": 0},
                "n3": {"origin": randint(0, 9), "mult": 0},
                "n4": {"origin": randint(0, 9), "mult": 0},
                "n5": {"origin": randint(0, 9), "mult": 0},
                "n6": {"origin": randint(0, 9), "mult": 0},
                "n7": {"origin": randint(0, 9), "mult": 0},
                "n8": {"origin": randint(0, 9), "mult": 0},
                "n9": {"origin": randint(0, 9), "mult": 0}
            }

            self.multiply_factor(numbers)

            dv_1 = self.extract_verifier(numbers)

            numbers["n10"] = {"origin": dv_1, "mult": 0}

            self.multiply_factor(numbers)

            dv_2 = self.extract_verifier(numbers)

            numbers["n11"] = {"origin": dv_2, "mult": 0}

            return "".join([str(it["origin"]) for it in numbers.values()])

    document_data = CPFDocumentDataGen()

    async def get_random_document(self) -> Data:
        cpf = await self.document_data.get_data()

        return CPF(cpf=cpf)

