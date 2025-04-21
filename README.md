# Maze Generator & Solver (Python + Tkinter 🧱🐍)

This is a visual maze generator and solver built using Python and Tkinter. It uses a depth-first search (DFS) algorithm to generate the maze and a recursive backtracking algorithm to solve it — all animated step by step.

## 🧩 Features

- Maze generation using DFS
- Step-by-step visual animation
- Recursive backtracking maze solving
- Live cell highlighting during traversal
- Color key:
  - 🟨 Yellow — current active cell
  - 🔴 Red line — forward move
  - ⚪ Gray line — backtracking
  - ⬜ Gray cell — visited but not part of solution path

## 🚀 How to Run

1. Make sure you have Python 3.10+ installed with Tkinter support.
2. Clone the repo or download the files.
3. Run the main file:

```bash
python3 main.py
```

## 🗂️ Project Structure

```
├── main.py         # Entry point
├── window.py       # Window and canvas management
├── point.py        # 2D coordinate class
├── line.py         # Line between two points
├── cell.py         # Represents a single maze cell
├── maze.py         # Maze generation and solving logic
├── tests.py        # Unit tests
```


## ⚙️ Dependencies

Python standard library only (tkinter, random, time, unittest)