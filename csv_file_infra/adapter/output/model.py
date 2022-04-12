from domain.model.entity import PersonName, Data


class PersonNameCSV(Data):

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

    def to_model(self) -> PersonName:
        return PersonName(name=self.group_name, variations=self.alternative_names, genre=self.classification)
