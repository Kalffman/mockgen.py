from pydantic import BaseModel

from domain.ports.input.model import PersonName, PersonFullName, Person, PersonDocument


class PersonNameDTO(BaseModel):
    name: str
    variations: list[str]
    genre: str


class PersonNameResponseDTO(BaseModel):
    data: PersonNameDTO


class PersonFullNameDTO(BaseModel):
    first_name: str
    last_name: str
    full_name: str


class PersonFullNameResponseDTO(BaseModel):
    data: PersonFullNameDTO


class PersonDocumentDTO(BaseModel):
    doc_type: str
    document: str


class PersonDocumentRespoonseDTO(BaseModel):
    data: PersonDocumentDTO


class PersonDTO(BaseModel):
    full_name: str
    cpf: str


class PersonResponseDTO(BaseModel):
    data: PersonDTO


class DTOParser:

    def parse_to_PersonNameDTO(self, person_name: PersonName) -> PersonNameDTO:
        return PersonNameDTO(
            name=person_name.name,
            variations=person_name.variations,
            genre=person_name.genre,
        )

    def parse_to_PersonFullNameDTO(self, person_full_name: PersonFullName) -> PersonFullNameDTO:
        return PersonFullNameDTO(
            full_name=person_full_name.full_name,
            first_name=person_full_name.first_name,
            last_name=person_full_name.last_name,
        )

    def parse_to_PersonDocumentDTO(self, person_document: PersonDocument) -> PersonDocumentDTO:
        return PersonDocumentDTO(
            doc_type=person_document.doc_type,
            document=person_document.document,
        )

    def parse_to_PersonDTO(self, person: Person) -> PersonDTO:
        return PersonDTO(
            full_name=person.name.full_name,
            cpf=person.get_document("CPF").document,
        )

    def parse_to_dto(self, model):
        if isinstance(model, Person):
            dto = PersonResponseDTO(data=self.parse_to_PersonDTO(model))
        elif isinstance(model, PersonName):
            dto = PersonNameResponseDTO(data=self.parse_to_PersonNameDTO(model))
        elif isinstance(model, PersonFullName):
            dto = PersonFullNameResponseDTO(data=self.parse_to_PersonFullNameDTO(model))
        elif isinstance(model, PersonDocument):
            dto = PersonDocumentRespoonseDTO(data=self.parse_to_PersonDocumentDTO(model))
        else:
            raise NotImplementedError(f"Não existe mapper para instancia de {model}")

        return dto
