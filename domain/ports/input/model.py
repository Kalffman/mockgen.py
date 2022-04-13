import abc

from domain import utils
import random


class PersonName:
    name: str
    variations: list[str]
    genre: str

    def __init__(self, **kwargs) -> None:
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def random_variation(self):
        if len(self.variations) > 1:
            s_random = random.SystemRandom()
            return s_random.choice(self.variations)
        else:
            return self.name


class PersonFullName:
    first_name: str
    last_name: str
    full_name: str

    def __init__(self, **kwargs) -> None:
        for key in kwargs:
            setattr(self, key, kwargs[key])

        self.full_name = utils.resolve_full_name(self.full_name)


class PersonDocument:
    doc_type: str
    document: str

    def __init__(self, **kwargs) -> None:
        for key in kwargs:
            setattr(self, key, kwargs[key])
