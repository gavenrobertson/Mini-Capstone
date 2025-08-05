import PySimpleGUI as sg
from gui import intro_window, student_window


def main():
    intro_view = intro_window()
    student_view = student_window()

    while True:
        event, values = intro_view.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        elif event in (sg.WINDOW_CLOSED, 'Next'):
            intro_view.close()
            while True:
                event, values = student_view.read()
                if event in (sg.WINDOW_CLOSED, 'Exit'):
                    break
                elif event in (sg.WINDOW_CLOSED, 'Submit'):
                    student_view.close()

if __name__ == '__main__':
    main()