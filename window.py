# Main layout program 
import PySimpleGUI as gui
from constants import *


mainLayout = [
    [
        gui.Text(NAME, font=("", 20, "bold"), justification='left', text_color=BLACK, background_color=WHITE)
    ],
    [
        gui.Text(key=MESSAGES, justification='center', text_color=BLACK, background_color=WHITE)
    ],
    [
        gui.Input(ZERO, key=OUTPUT, justification='right', background_color=DISPLAY, text_color=BLACK, size=(22, 2), pad=(0, 0), font=(FONT, 20, "bold"))
    ],
    [
        gui.Button(CLEAR, button_color=(WHITE , SECONDARY), size=SIZE_BTN, pad=(0, 0), border_width=1), 
        gui.Button(SQUARE_ROOT, button_color=(BLACK, GRAY), size=SIZE_BTN, pad=(0,0)),
        gui.Button(PERCETAGE, button_color=(BLACK, GRAY), size=SIZE_BTN, pad=(0,0)), 
        gui.Button(DIVIDE, button_color=(BLACK, GRAY), size=SIZE_BTN, pad=(0, 0))
    ],
    [
        gui.Button(SEVEN, button_color=(BLACK , WHITE), size=SIZE_BTN, pad=(0, 0)), 
        gui.Button(EIGHT, button_color=(BLACK , WHITE), size=SIZE_BTN, pad=(0, 0)), 
        gui.Button(NINE, button_color=(BLACK , WHITE), size=SIZE_BTN, pad=(0, 0)), 
        gui.Button(MULTIPLY, button_color=(BLACK, GRAY), size=SIZE_BTN, pad=(0, 0))
    ],
    [
        gui.Button(FOUR, button_color=(BLACK , WHITE), size=SIZE_BTN, pad=(0, 0)), 
        gui.Button(FIVE, button_color=(BLACK , WHITE), size=SIZE_BTN, pad=(0, 0)), 
        gui.Button(SIX, button_color=(BLACK , WHITE), size=SIZE_BTN, pad=(0, 0)), 
        gui.Button(MINUS, button_color=(BLACK, GRAY), size=SIZE_BTN, pad=(0, 0))
    ],
    [
        gui.Button(ONE, button_color=(BLACK , WHITE), size=SIZE_BTN, pad=(0, 0)), 
        gui.Button(TWO, button_color=(BLACK , WHITE), size=SIZE_BTN, pad=(0, 0)), 
        gui.Button(THREE, button_color=(BLACK , WHITE), size=SIZE_BTN, pad=(0, 0)), 
        gui.Button(PLUS, button_color=(BLACK, GRAY), size=SIZE_BTN, pad=(0, 0))
    ],
    [
        gui.Button(PLUS_MINUS, button_color=(BLACK , WHITE), size=SIZE_BTN, pad=(0, 0)), 
        gui.Button(ZERO, button_color=(BLACK , WHITE), size=SIZE_BTN, pad=(0, 0)), 
        gui.Button(DOT, button_color=(BLACK , WHITE), size=SIZE_BTN, pad=(0, 0)), 
        gui.Button(EQUAL, button_color=(WHITE , TERTIARY), size=SIZE_BTN, pad=(0, 0))
    ],
]
# Window
screen = gui.Window(
    title=TITLE, 
    layout=mainLayout, 
    background_color="#F4F4FB",
    resizable=False,
    text_justification='right',
    auto_size_text=True,
    return_keyboard_events=True,
)