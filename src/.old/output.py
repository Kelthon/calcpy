from constants import *

# verify if value is a number
def isSymbol (value):
    for i in SYMBOLS:
        if value == i:
            return True
    return False

# add numbers to output
def addNumberToOutput(screen, values, output, valueEntry, valueNull=ZERO):
    if values[output] == valueNull:
        screen[output].update(valueEntry)
    else:
        expression = values[output] + valueEntry
        screen[output].update(expression)

# add symbols to output
def addSymbolToOutput(screen, values, output, symbol):
    endsWithSymbol = False
    
    expression = values[output]
    if isSymbol(expression[-1]):
        endsWithSymbol = True
        
    if expression[-1] == symbol or endsWithSymbol:
        expression = expression[:-1] + symbol
    else:
        expression = expression + symbol
    screen[output].update(expression)

# update output
def setResult(screen, output, result):
    screen[output].update(str(result))
