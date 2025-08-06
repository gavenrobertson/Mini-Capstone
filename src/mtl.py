import PySimpleGUI as sg
import csv

CSV_FILE = r"assets/data/form_4392_full.csv"  # static file
sg.theme('DarkBlue1')

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

def save_csv(file_path, headings, rows):
    """Save updated CSV back to file."""
    try:
        with open(file_path, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headings)  # write header
            writer.writerows(rows)     # write rows
    except Exception as e:
        sg.popup_error(f"Error saving CSV file:\n{e}")

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
        select_mode=sg.TABLE_SELECT_MODE_BROWSE,
        vertical_scroll_only=False,
    )],
    [sg.Button("Delete Selected Row"), sg.Button("Exit")]
    ###[sg.Button("Exit")]
]

window = sg.Window("MTL 4392 Viewer", layout, resizable=True, size=(900, 245))

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
    if event == "Delete Selected Row":
        selected = values["-TABLE-"]
        if selected:
            row_index = selected[0]  # Get selected row index
            del rows[row_index]      # Remove from list
            save_csv(CSV_FILE, headings, rows)  # Save back to CSV
            window["-TABLE-"].update(values=rows)  # Refresh table
        else:
            sg.popup("Please select a row to delete!")
window.close()
