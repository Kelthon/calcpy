from src.proccess.operation.op import Operation
from src.proccess.stack import Stack

class NumberAddOperation(Operation):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, token: chr) -> None:
        self.__buffer.push(token)

    def solve(self) -> Stack:
        return self.__buffer