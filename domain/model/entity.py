

class PersonName:
    name: str
    variations: list[str]

    def __init__(self, **kwargs) -> None:
        for key in kwargs:
            setattr(self, key, kwargs[key])

