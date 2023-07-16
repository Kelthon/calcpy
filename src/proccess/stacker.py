
from src.proccess.operation.op import Operation
from src.proccess.syntax_stack import SyntaxStack
from src.proccess.operation.number import NumberAddOperation

def toExpr(expr: str):
    return expr.replace(" ", "")[::-1]


class Stacker:
    __stack: SyntaxStack = SyntaxStack()
    __operation: Operation = NumberAddOperation()

    @classmethod
    def setOperation(cls, op: Operation) -> None:
        cls.__operation = op

    @classmethod
    def read(cls, expression: str):

        for char in expression:
            if char.isdigit():
                cls.__stack.push(cls.__operation.solve())
                cls.setOperation(NumberAddOperation())

            elif char == '+':
                pass

            else:
                pass

            cls.__operation.execute(char)

        print(cls.__stack)