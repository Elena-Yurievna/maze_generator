from window import Window
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(
        x1=50,
        y1=50,
        num_rows=5,
        num_cols=5,
        cell_size_x=50,
        cell_size_y=50,
        win=win,
        seed=0
    )
    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()