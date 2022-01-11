from tkinter import constants
import PySimpleGUI as gui
from constants import *
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED, Print


def isSymbol (value):
    for i in SYMBOLS:
        if value == i:
            return True
    return False

def addNumberToOutput(screen, values, output, valueEntry, valueNull=ZERO):
    if values[output] == valueNull:
        screen[OUTPUT].update(valueEntry)
    else:
        expression = values[output] + valueEntry
        screen[output].update(expression)

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

def setResult(screen, output, result):
    screen[output].update(str(result))

def mainWindow():
    # Main layout program 
    mainLayout = [
        [gui.Text(key=MESSAGES)],
        [gui.Input(ZERO, key=OUTPUT,)],
        [gui.Button(CLEAR), gui.Button(SQUARE_ROOT), gui.Button(PERCETAGE), gui.Button(DIVIDE)],
        [gui.Button(SEVEN), gui.Button(EIGHT), gui.Button(NINE), gui.Button(MULTIPLY)],
        [gui.Button(FOUR), gui.Button(FIVE), gui.Button(SIX), gui.Button(MINUS)],
        [gui.Button(ONE), gui.Button(TWO), gui.Button(THREE), gui.Button(PLUS)],
        [gui.Button(PLUS_MINUS), gui.Button(ZERO), gui.Button(DOT), gui.Button(EQUAL)],
    ]
    # Window
    screen = gui.Window("Calculadora", mainLayout)

    # Global Vars
    numberOne = 0       # RegisterA
    numberTwo = 0       # RegisterB
    strNumber:str = ZERO    # Buffer
    operation:str = EQS     # Operation
    addedNumber = False # True if RegisterA contains a number

    # Main loop
    while True:
        # Get events and values
        event, values = screen.Read(timeout = 250)

        # Close program
        if event == WINDOW_CLOSED:
            screen.close()
            break
        
        # Clear output
        if event == CLEAR:
            numberOne = 0
            numberTwo = 0
            strNumber = ZERO
            addedNumber = False
            screen[OUTPUT].update(ZERO)
        
        # Add numbers
        for number in NUMBERS:
            # print(strNumber, number)
            if number == event:
                strNumber = strNumber + number if strNumber != ZERO else number
                addNumberToOutput(screen, values, OUTPUT, number)
        
        # Add symbols
        if event == DOT:
            symbol = BASIC_OPERATIONS[operation] if addedNumber else PLUS
            strNumber = strNumber + DOT if strNumber.count(DOT) == 0 else strNumber
            strResult = strNumber if not addedNumber else str(numberOne) + symbol + strNumber
            setResult(screen, OUTPUT, strResult)

        defaults_operations = BASIC_OPERATIONS
        for i, j in defaults_operations.items():
            if j == event:
                if addedNumber == False:
                    numberOne = float(strNumber)
                    addedNumber = True
                    strNumber = ZERO
                    operation = i
                    addSymbolToOutput(screen, values, OUTPUT, j)
                else:
                    numberTwo = float(strNumber)
                    try:
                        if operation == SUM:
                            numberOne = numberOne + numberTwo
                        elif operation == DIF:
                            numberOne = numberOne - numberTwo
                        elif operation == MUL:
                            numberOne = numberOne * numberTwo
                        elif operation == DIV:
                            numberOne = numberOne / numberTwo
                    except:
                        numberOne = 0
                        setResult(screen, MESSAGES, ERR)
                    strNumber = str(numberOne)
                    numberTwo = 0
                    addedNumber = False
                    setResult(screen, OUTPUT, numberOne)
        if event == PLUS_MINUS:
            operation = EQS
            result = float(strNumber) * -1
            if addedNumber:
                strResult = str(numberOne) + str(result) if result < 0 else str(numberOne) + PLUS + str(result)
                strNumber = str(result)
            else:
                strResult = strNumber = str(result)
            setResult(screen, OUTPUT, strResult)
        
        if event == EQUAL:
            result = 0
            if operation == EQS:
                result = float(strNumber)
            elif operation == SUM:
                numberTwo = float(strNumber)
                result = numberOne + numberTwo
            elif operation == DIF:
                numberTwo = float(strNumber)
                result = numberOne - numberTwo
            elif operation == MUL:
                numberTwo = float(strNumber)
                result = numberOne * numberTwo
            elif operation == DIV:
                numberTwo = float(strNumber)
                try:
                    result = numberOne / numberTwo
                except:
                    numberOne = result = 0
                    setResult(screen, MESSAGES, ZERO_DIV_ERR)

            setResult(screen, MESSAGES, VOID)
            operation = EQS
            numberTwo = 0
            strNumber = str(result)
            setResult(screen, OUTPUT, result)
        
        if event == POW:
            if addedNumber == False:
                numberOne = float(strNumber)
                addedNumber = True
                strNumber = ZERO
                operation = POW
                addSymbolToOutput(screen, values, OUTPUT, CARET)
            else:
                numberTwo = float(strNumber)
                numberOne = result = numberOne ** numberTwo
                strNumber = str(result)        
                numberTwo = 0
                setResult(screen, OUTPUT, result)
        
        if event == SQUARE_ROOT:
            numberOne = float(strNumber)
            numberOne = numberOne ** (1/2)
            strNumber = str(numberOne)
            setResult(screen, OUTPUT, numberOne)

        if event == PERCETAGE:
            numberOne = float(strNumber)
            numberOne = numberOne / 100
            strNumber = str(numberOne)
            setResult(screen, OUTPUT, numberOne)

    screen.Close()
mainWindow()
