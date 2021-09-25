import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED

def mainWindow():
    mainLayout = [
        [gui.Input("0")],
        [gui.Button("Clear")],
    ]

    screen = gui.Window("Calculadora", mainLayout)

    while True:
        event, values = screen.Read(timeout = 250)

        if event == WINDOW_CLOSED:
            screen.close()
            break
    screen.exit()

mainWindow()