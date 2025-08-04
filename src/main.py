from gui import create_window
import PySimpleGUI as sg

def main():
    window = create_window()

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        # You can process events here
        print(f"Event: {event}, Values: {values}")

    window.close()

if __name__ == '__main__':
    main()