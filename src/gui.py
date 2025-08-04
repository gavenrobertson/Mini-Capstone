import PySimpleGUI as sg

def create_window():
    layout = [
        [sg.Text('Enter something:'), sg.Input(key='-INPUT-')],
        [sg.Button('Submit'), sg.Button('Exit')]
    ]
    return sg.Window('My PySimpleGUI App', layout)