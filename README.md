# Python Arcade

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Python Arcade** is a terminal-based collection of interactive mini-games and utility tools built using Python. From classic casino-style games like Slot Machines to handy utilities like QR Code Generators, everything is accessible through an easy-to-navigate command-line interface menu.

---

## Included Apps & Games

### Utilities
* **ATM Simulator (old ver):** Manage virtual deposits, withdrawals, and check account transaction history secured by a PIN.
* **ATM Simulator (new ver):** Along with all functions of the old ver, allows multi-account management, inter-account transactions.
* **Currency Converter:** Convert values between USD, EUR, and CAD with real-time history tracking.
* **QR Code Generator:** Generate custom QR code images with customized colors and save them directly to your machine.
* **Text Editor:** A simple CLI text editor allowing you to write, overwrite, or append content to files.
* **To-Do App:** Keep track of your daily tasks and to-do lists.

### Games
* **Slot Machine:** A multi-symbol casino slot game featuring animated reel spins, bets, and payout multipliers.
* **Pig Dice:** A multi-player turn-based risk-and-reward dice game where rolling a `1` clears your turn's points.
* **Number Guessing:** Test your luck against configurable minimum/maximum ranges with limited attempts and best-score tracking.
* **Dice Roll Simulator:** Roll any number of dice simultaneously and track your total roll history.
* **Word Guessing:** Classic word-puzzle game in the terminal.

---

## Repository Structure

```text
python-arcade/
│
├── main.py                   # Central interactive menu loop
└── modules/                  # Package containing all individual tools/games
    ├── atm_sim_old.py
    ├── atm_sim_new.py
    ├── currency_convertor.py
    ├── dice_roll.py
    ├── number_guessing.py
    ├── pig_dice.py
    ├── qrcode_gen.py
    ├── slot_machine.py
    ├── text_editor.py
    ├── to_do_app.py
    └── word_guessing.py
```
## Getting Started
### Prerequisites
* Python 3.7.1 or higher installed on your computer.
* Essential libraries installed (e.g., qrcode, pillow).

### Installation & Setup
1. Clone the repository:
```
git clone [https://github.com/satyam-kumar-singh-sys/python-arcade.git](https://github.com/satyam-kumar-singh-sys/python-arcade.git)
cd python-arcade
```
2. Install required dependencies:
```
pip install qrcode pillow
```
3. Run the application:
```
python main.py
```
## How to Play
Upon executing main.py, you will see the interactive terminal menu:
```
==========================
Welcome to Python Arcade!
==========================
1. ATM Simulator (Old ver)
2. ATM Simulator (New Ver
3. Currency Convertor
4. QR Code Generator
5. Text Editor
6. To Do App
7. Dice Roll
8. Word Guessing
9. Number Guessing
10.Pig Dice
11.Slot Machine
12.Exit
==========================
```
Simply type the number corresponding to the tool or game you wish to run and press Enter!

## License
This project is open-source and available under the MIT License.
