from src.proccess.stack import Stack

class SyntaxStack(Stack):
    def __init__(self) -> None:
        super().__init__()

    def push(self, stack: Stack) -> None:
        return super().push(stack)
    
    def pop(self) -> Stack:
        return super().pop()
    