---

# 🎮 Tic-Tac-Toe Client-Server Game

This project implements a client-server version of the classic Tic-Tac-Toe game using socket programming in Python. The game allows players to choose different board sizes and uses 'S' and 'O' symbols.

## 📋 Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)

## 🚀 Installation

1. **Clone the repository**:
    ```bash
    git clone [https://github.com/Manoj-Kumar-BV/Tic-Tac-Toe_Client-Server_Game]
    cd tic-tac-toe-client-server
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 🎮 Usage

1. **Start the server**:
    ```bash
    python server.py
    ```

2. **Start the client** (in a separate terminal or machine):
    ```bash
    python client.py
    ```

3. **Follow the prompts** to play the game.

## ✨ Features

- **Multiplayer**: Play Tic-Tac-Toe with another player over a network.
- **Custom Board Sizes**: Choose different board sizes (e.g., 3x3, 6x6).
- **Custom Symbols**: Use 'S' and 'O' instead of the traditional 'X' and 'O'.
- **Rematch Option**: Players can choose to play again after a game ends.

## 📁 Project Structure

```
.
├── client.py
├── server.py
├── tic_tac_toe.py  # Contains the TicTacToe class definition
├── README.md
└── requirements.txt  # List of dependencies
```

## 🛠️ Dependencies

- **Python 3.x**
- **socket** (standard library)
- **pickle** (standard library)

To install dependencies, run:
```bash
pip install -r requirements.txt
```

---
