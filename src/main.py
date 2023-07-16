from src.proccess.stacker import Stacker, toExpr

expr = toExpr("3 / 2 ^ (2 + 2) - 1")
Stacker.read(expr)
print(expr)