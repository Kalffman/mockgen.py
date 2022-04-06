import re
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

        self.full_name = re.sub(' +', ' ', self.full_name)

        full_name_arr = re.split('\\s', self.full_name)

        spaces = len(full_name_arr) - 1

        if spaces >= 3:
            full_name_arr.insert(-2, "DE")

            self.full_name = " ".join(full_name_arr)

        elif spaces > 1:
            full_name_arr.insert(-1, "DE")

            self.full_name = " ".join(full_name_arr)

