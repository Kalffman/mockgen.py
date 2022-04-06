from pydantic import BaseModel


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
