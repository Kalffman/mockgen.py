import abc


class Data(abc.ABC):

    def __init__(self, **kwargs) -> None:
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @abc.abstractmethod
    def to_model(self) -> any:
        raise NotImplementedError
