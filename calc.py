from tkinter.constants import TRUE
import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import T, WINDOW_CLOSED, Window

def addNumberToOutput(screen, values, output, valueEntry, valueNull = '0', valueDot='.'):
    if values[output] == valueNull:
        screen['output'].update(valueEntry)
    else:
        expression = values[output] + valueEntry
        screen[output].update(expression)

def addSymbolToOutput(screen, values, output, symbol, valueDot='.'):
    float_number = False

    for i in values[output]:
        if i == valueDot:
            float_number = TRUE

    if symbol == valueDot:
        if not float_number:
            expression = values[output] + symbol
            screen[output].update(expression)
    else: 
        expression = values[output] + symbol
        screen[output].update(expression)

def mainWindow():
    mainLayout = [
        [gui.Input("0", key='output')],
        [gui.Button("C"), gui.Button("-/^"), gui.Button("%"), gui.Button("/")],
        [gui.Button("7"), gui.Button("8"), gui.Button("9"), gui.Button("x")],
        [gui.Button("4"), gui.Button("5"), gui.Button("6"), gui.Button("-")],
        [gui.Button("1"), gui.Button("2"), gui.Button("3"), gui.Button("+")],
        [gui.Button("+/-"), gui.Button("0"), gui.Button("."), gui.Button("=")],
    ]

    screen = gui.Window("Calculadora", mainLayout)


        
    while True:
        event, values = screen.Read(timeout = 250)

        if event == WINDOW_CLOSED:
            screen.close()
            break

        if event == 'C':
            screen['output'].update("0")

        if event == '1':
            addNumberToOutput(screen, values, 'output', '1')
        if event == '2':
            addNumberToOutput(screen, values, 'output', '2')
        if event == '3':
            addNumberToOutput(screen, values, 'output', '3')
        if event == '4':
            addNumberToOutput(screen, values, 'output', '4')
        if event == '5':
            addNumberToOutput(screen, values, 'output', '5')
        if event == '6':
            addNumberToOutput(screen, values, 'output', '6')
        if event == '7':
            addNumberToOutput(screen, values, 'output', '7')
        if event == '8':
            addNumberToOutput(screen, values, 'output', '8')
        if event == '9':
            addNumberToOutput(screen, values, 'output', '9')
        if event == '0':
            addNumberToOutput(screen, values, 'output', '0')
        if event == '.':
            addSymbolToOutput(screen, values, 'output', '.')
        if event == '+':
            addSymbolToOutput(screen, values, 'output', '+')
            
    screen.Close()
mainWindow()
