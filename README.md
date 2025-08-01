# Mini-Capstone

## 🚀 Getting Started


### Clone the repo
git clone (https://github.com/gavenrobertson/Mini-Capstone.git)
cd my_game_project

### Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Install dependencies
pip install -r requirements.txt

### Run the game
python src/main.py

---

## 📁 Project Structure
```
my_game_project/
├── assets/
│ ├── images/
│ ├── sounds/
│ ├── fonts/
│ └── levels/
├── src/
│ ├── init.py
│ ├── main.py # Entry point for the game
│ ├── settings.py # Game settings (screen size, FPS, etc.)
│ ├── game.py # Main Game class
│ ├── player.py # Player class
│ ├── enemy.py # Enemy logic
│ ├── level.py # Level management
│ └── utils.py # Helper functions
├── README.md
└── requirements.txt
```
---

## 📂 Folders Overview

### `assets/`
Contains all the static game assets:

- **images/** – Sprites, background images, UI elements.
- **sounds/** – Sound effects and background music.
- **fonts/** – Custom fonts used in the game.
- **levels/** – JSON, CSV, or other formats that define level layouts.

### `src/`
Contains the core game logic and code:

- **`main.py`** – The entry point of the game. Initializes and runs the game loop.
- **`settings.py`** – Stores configuration constants like screen size, FPS, and color definitions.
- **`game.py`** – The central Game class that manages state, input, and drawing.
- **`player.py`** – The Player class and its related logic.
- **`enemy.py`** – Contains enemy behavior and interactions.
- **`level.py`** – Manages levels, loading, and progression.
- **`utils.py`** – General helper functions such as collision checks, asset loading, etc.

---

## 📦 Other Files

- **`README.md`** – You're reading it!
- **`requirements.txt`** – List of required Python packages (e.g., `pygame`, etc.).

---

## ✅ Optional Additions

- **`data/`** – For saving player data, high scores, etc.
- **`tests/`** – For unit tests (if using `pytest` or similar).
