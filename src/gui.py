import PySimpleGUI as sg

def intro_window():
    layout = [
        [sg.Text('Welcome, please enter the below information!')],
        [sg.Text('Name: '), sg.Input(key='-NAME-')],
        [sg.Text('Email: '), sg.Input(key='-EMAIL-')],
        [sg.Text('Rank: '), sg.Input(key='-RANK-')],
        [sg.Button('Submit'), sg.Button('Exit')]
    ]
    return sg.Window('My PySimpleGUI App', layout)

def student_window():
    layout = [
        [sg.Text('Welcome, please enter the below information!')],
        [sg.Text('More: '), sg.Input(key='-MORE-')],
        [sg.Text('PLUS: '), sg.Input(key='-PLUS-')],
        [sg.Button('Submit'), sg.Button('Exit')]
    ]
    return sg.Window('4392 Request: ', layout)