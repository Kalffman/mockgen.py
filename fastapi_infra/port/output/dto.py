from pydantic import BaseModel


class PersonNameCSV:
    alternative_names: list[str]
    classification: str
    first_name: str
    frequency_female: str
    frequency_male: str
    frequency_total: str
    frequency_group: str
    group_name: str
    ratio: float

    def __init__(self, **data) -> None:
        for key in data:
            setattr(self, key, data[key])


class PersonNameDTO(BaseModel):
    name: str
    variations: list[str]


class PersonNameResponseDTO(BaseModel):
    data: PersonNameDTO
