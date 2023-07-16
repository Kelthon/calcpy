from abc import ABC, abstractmethod
from typing import Any

class Event(ABC):
    def __init__(self, type: str) -> None:
        self.__type = type

    @property
    def type(self):
        return self.__type

    @abstractmethod
    def update(self, data: Any) -> None:
        pass

    def __str__(self) -> str:
        return f"Event(type: '{self.type}')"