# First App using PySimpleGUI

import PySimpleGUI as psg

psg.theme('Python')


# Layout
layout = [[psg.Text("Hello World")], [psg.Button("OK")]]

#window
window = psg.Window(title="Hello World", layout=layout, margins=(100, 100))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == psg.WIN_CLOSED:
        break


window.close()
