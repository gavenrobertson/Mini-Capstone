# Mini-Capstone

## 🚀 Getting Started


### Clone the repo
git clone (https://github.com/gavenrobertson/Mini-Capstone.git)
cd my_game_project

### Install dependencies
pip install -r requirements.txt

### Run the game
python src/main.py

---

## 📁 Project Structure
```
my_gui_app/
├── src/
│   ├── __init__.py
│   ├── main.py           # Entry point of the application
│   ├── gui.py            # GUI layout and interaction logic
│   ├── settings.py       # App-wide constants and configuration
│   └── utils.py          # Helper functions
├── README.md
└── requirements.txt
```
---

## 📂 Folders Overview

### `assets/`
Contains all the static game assets:

- **images/** – Sprites, background images, UI elements.
- **data/** – JSON, CSV, or text files used by the app.
- **fonts/** – Custom fonts used in the game.

### `src/`
Contains the core game logic and code:

- **`main.py`** – The entry point of the game. Initializes and runs the game loop.
- **`gui.py`** – Builds and manages PySimpleGUI window(s) and handles interactions.
- **`settings.py`** – Stores configuration constants like screen size, FPS, and color definitions.
- **`utils.py`** – General helper functions such as collision checks, asset loading, etc.

---

## 📦 Other Files

- **`README.md`** – You're reading it!
- **`requirements.txt`** – List of required Python packages (e.g., `pygame`, etc.).
