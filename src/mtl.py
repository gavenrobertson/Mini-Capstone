import PySimpleGUI as sg
import csv

CSV_FILE = r"C:\Users\Student\Desktop\New folder\Mini-Capstone\assets\data\fortythree92.csv"  # static file

def load_csv(file_path):
    try:
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            if data:
                headings = data[0]
                rows = data[1:]
                return headings, rows
    except Exception as e:
        sg.popup_error(f"Error reading CSV file:\n{e}")
    return [], []

def show_row_details(row, headings):
    """Opens a new window showing details of the selected row."""
    layout = [
        [sg.Text(f"{headings[i]}: {value}")] for i, value in enumerate(row)
    ] + [[sg.Button("Close")]]
    
    win = sg.Window("MTL Details", layout, modal=True)
    while True:
        ev, _ = win.read()
        if ev in (sg.WINDOW_CLOSED, "Close"):
            break
    win.close()

# Load CSV
headings, rows = load_csv(CSV_FILE)

layout = [
    [sg.Table(
        values=rows,
        headings=headings,
        auto_size_columns=True,
        justification="left",
        num_rows=15,
        key="-TABLE-",
        enable_events=True,  # Detect clicks
        select_mode=sg.TABLE_SELECT_MODE_BROWSE
    )],
    [sg.Button("Exit")]
]

window = sg.Window("CSV Viewer", layout, resizable=True)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    if event == "-TABLE-":  # Row clicked
        selected = values["-TABLE-"]
        if selected:
            row_index = selected[0]
            row_data = rows[row_index]
            show_row_details(row_data, headings)

window.close()
