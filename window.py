# Main layout program 
import PySimpleGUI as gui
from constants import *

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
screen = gui.Window(NAME, mainLayout)