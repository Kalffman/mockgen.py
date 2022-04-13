from algorithm_infra.adapter.output.model import CPF
from domain.ports.output.model import Data
from domain.ports.output.data_access import PersonDocumentDataAccessPort, ResourceData
from random import randint


class CPFDataAccessGenerator(PersonDocumentDataAccessPort):

    class CPFDocumentDataGen(ResourceData):

        @staticmethod
        def extract_verifier(numbers: dict):
            dv_1 = 0

            for it in numbers.values():
                dv_1 += it["mult"]

            dv_1 = 11 - divmod(dv_1, 11)[1]

            return 0 if dv_1 >= 10 else dv_1

        @staticmethod
        def multiply_factor(numbers: dict):
            for idx, it in enumerate(numbers):
                fac = 10 - idx

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

