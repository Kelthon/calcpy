from abc import ABC, abstractmethod
from src.proccess.stack import Stack

class Operation(ABC):
    def __init__(self) -> None:
        self.__buffer: Stack = Stack()

    @abstractmethod
    def execute(self, data: chr) -> None:
        pass

    @abstractmethod
    def solve(self) -> Stack:
        pass