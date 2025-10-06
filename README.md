# Gomoku: Player vs AI

Gomoku is a classic strategy board game played on a 15×15 grid. Two players take turns placing their pieces, aiming to be the first to form an unbroken line of five—horizontally, vertically, or diagonally. This implementation allows a **player to compete against an AI** with a simple heuristic strategy.

---

## Game Features

- Player vs AI on a 15×15 grid.
- AI blocks the player from forming 5 in a row and tries to complete its own line.
- Graphical interface built with **Pygame**.
- Game ends when **five consecutive pieces** are aligned.
- Winner is displayed on the screen.

---

## How to Play

1. Run the Python file using Python 3.x with Pygame installed.
2. Click on any empty cell to place your piece (green color).
3. The AI (red color) will automatically make its move after yours.
4. The first to align 5 pieces in a row wins.
5. Close the window to exit the game.

---

## Requirements

- Python 3.x
- Pygame

Install Pygame if you haven't:

```bash
pip install pygame
