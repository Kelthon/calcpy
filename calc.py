import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED

def isSymbol (value, dotSymbol='.', plusSymbol='+', minusSymbol='-', multSymbol='*', divSymbol='/', pRightSymbol='(', pLeftSymbol=')'):
    if value == dotSymbol or  value == plusSymbol:
        return True
    if value == minusSymbol or value == multSymbol:
        return True
    if value == divSymbol or value == pRightSymbol:
        return True
    if value == pLeftSymbol:
        return True
    return False

def addNumberToOutput(screen, values, output, valueEntry, valueNull = '0', valueDot='.'):
    if values[output] == valueNull:
        screen['output'].update(valueEntry)
    else:
        expression = values[output] + valueEntry
        screen[output].update(expression)

def addSymbolToOutput(screen, values, output, symbol, dotSymbol='.', plusSymbol='+', minusSymbol='-', multSymbol='*', divSymbol='/'):
    float_number = False
    endsWithSymbol = False

    for i in values[output]:
        if i == dotSymbol:
            float_number = True 

    expression = values[output]
    if isSymbol(expression[-1]):
        endsWithSymbol = True
        
    if symbol == dotSymbol:
        if not float_number:
            if not endsWithSymbol:
                expression = values[output] + symbol
            else:
                expression = expression[:-1] + symbol
            screen[output].update(expression)
    else:
        if expression[-1] == symbol or endsWithSymbol:
            expression = expression[:-1] + symbol
            
        else:
            expression = expression + symbol
    screen[output].update(expression)

def setResult(screen, output, result):
    screen[output].update(str(result))

def mainWindow():
    mainLayout = [
        [gui.Text(key='message')],
        [gui.Input("0", key='output',)],
        [gui.Button("C"), gui.Button("-/^"), gui.Button("%"), gui.Button("/")],
        [gui.Button("7"), gui.Button("8"), gui.Button("9"), gui.Button("x")],
        [gui.Button("4"), gui.Button("5"), gui.Button("6"), gui.Button("-")],
        [gui.Button("1"), gui.Button("2"), gui.Button("3"), gui.Button("+")],
        [gui.Button("±"), gui.Button("0"), gui.Button("."), gui.Button("=")],
    ]

    screen = gui.Window("Calculadora", mainLayout)
        
    numberOne = 0
    numberTwo = 0
    addedNumber = False
    strNumber = '0'
    operation = 'equals'

    while True:
        event, values = screen.Read(timeout = 250)
        if event == WINDOW_CLOSED:
            screen.close()
            break
        # Clear output
        if event == 'C':
            numberOne = 0
            numberTwo = 0
            strNumber = '0'
            addedNumber = False
            screen['output'].update("0")
        # Add numbers
        if event == '1':
            strNumber = strNumber + '1'
            addNumberToOutput(screen, values, 'output', '1')
        if event == '2':
            strNumber = strNumber + '2'
            addNumberToOutput(screen, values, 'output', '2')
        if event == '3':
            strNumber = strNumber + '3'
            addNumberToOutput(screen, values, 'output', '3')
        if event == '4':
            strNumber = strNumber + '4'
            addNumberToOutput(screen, values, 'output', '4')
        if event == '5':
            strNumber = strNumber + '5'
            addNumberToOutput(screen, values, 'output', '5')
        if event == '6':
            strNumber = strNumber + '6'
            addNumberToOutput(screen, values, 'output', '6')
        if event == '7':
            strNumber = strNumber + '7'
            addNumberToOutput(screen, values, 'output', '7')
        if event == '8':
            strNumber = strNumber + '8'
            addNumberToOutput(screen, values, 'output', '8')
        if event == '9':
            strNumber = strNumber + '9'
            addNumberToOutput(screen, values, 'output', '9')
        if event == '0':
            strNumber = strNumber + '0'
            addNumberToOutput(screen, values, 'output', '0')
        # add symbols
        # fix dot not added
        if event == '.':
            if strNumber.count('.') == 0:    
                strNumber = strNumber + '.'
            addSymbolToOutput(screen, values, 'output', '.')
        if event == '+':
            if addedNumber == False:
                numberOne = float(strNumber)
                addedNumber = True
                strNumber = '0'
                operation = 'sum'
                addSymbolToOutput(screen, values, 'output', '+')
            else:
                numberTwo = float(strNumber)
                numberOne = result = numberOne + numberTwo
                strNumber = str(result)        
                numberTwo = 0
                addedNumber = False
                setResult(screen, 'output', result)
        if event == '-':
            if addedNumber == False:
                numberOne = float(strNumber)
                addedNumber = True
                strNumber = '0'
                operation = 'dif'
                addSymbolToOutput(screen, values, 'output', '-')
            else:
                numberTwo = float(strNumber)
                numberOne = result = numberOne - numberTwo
                strNumber = str(result)        
                numberTwo = 0
                addedNumber = False
                setResult(screen, 'output', result)
        if event == 'x':
            if addedNumber == False:
                numberOne = float(strNumber)
                addedNumber = True
                strNumber = '0'
                operation = 'mult'
                addSymbolToOutput(screen, values, 'output', '*')
            else:
                numberTwo = float(strNumber)
                numberOne = result = numberOne * numberTwo
                strNumber = str(result)        
                numberTwo = 0
                addedNumber = False
                setResult(screen, 'output', result)
        if event == '/':
            if addedNumber == False:
                numberOne = float(strNumber)
                addedNumber = True
                strNumber = '0'
                operation = 'div'
                addSymbolToOutput(screen, values, 'output', '/')
            else:
                numberTwo = float(strNumber)
                try:
                    numberOne = result = numberOne / numberTwo
                    strResult = str(result)
                except:
                    strResult = "Error"
                    numberOne = result = 0
                strNumber = strResult        
                numberTwo = 0
                addedNumber = False
                setResult(screen, 'output', strResult)
        if event == '±':
            operation = 'equals'
            result = float(strNumber) * -1
            if addedNumber:
                strResult = str(numberOne) + str(result) if result < 0 else str(numberOne) + '+' + str(result)
                strNumber = str(result)
            else:
                strResult = strNumber = str(result)
            setResult(screen, 'output', strResult)
        if event == '=':
            result = 0
            if operation == 'equals':
                setResult(screen, "message", "")
                result = float(strNumber)
            elif operation == 'sum':
                setResult(screen, "message", "")
                numberTwo = float(strNumber)
                result = numberOne + numberTwo
            elif operation == 'dif':
                setResult(screen, "message", "")
                numberTwo = float(strNumber)
                result = numberOne - numberTwo
            elif operation == 'mult':
                setResult(screen, "message", "")
                numberTwo = float(strNumber)
                result = numberOne * numberTwo
            elif operation == 'div':
                numberTwo = float(strNumber)
                try:
                    result = numberOne / numberTwo
                except:
                    setResult(screen, "message", "Erro divisão por zero")

            operation = 'equals'
            numberTwo = 0
            addedNumber = False
            strNumber = result
            setResult(screen, 'output', result)
    screen.Close()
mainWindow()
