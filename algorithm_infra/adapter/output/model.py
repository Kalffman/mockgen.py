from domain.ports.input.model import PersonDocument
from domain.ports.output.model import Data


class CPF(Data):
    cpf: str

    def to_model(self) -> PersonDocument:
        return PersonDocument(doc_type="CPF", document=self.cpf)
