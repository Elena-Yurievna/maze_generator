import time
from cell import Cell
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._rows = num_rows
        self._cols = num_cols
        self._cell_width = cell_size_x
        self._cell_height = cell_size_y
        self._win = win
        self._cells = []
        
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
    
    def _create_cells(self):
        for i in range(self._cols):
            column = []
            for j in range(self._rows):
                cell = Cell(0, 0, 0, 0, self._win)
                column.append(cell)
            self._cells.append(column)

        for i in range(self._cols):
            for j in range(self._rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self._x1 + i * self._cell_width
        y1 = self._y1 + j * self._cell_height
        x2 = x1 + self._cell_width
        y2 = y1 + self._cell_height

        cell = self._cells[i][j]
        cell._x1 = x1
        cell._y1 = y1
        cell._x2 = x2
        cell._y2 = y2

        cell.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        self._draw_cell(0, 0)

        exit_cell = self._cells[self._cols - 1][self._rows - 1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._cols - 1, self._rows - 1)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True

        while True:
            neighbors = []

            if i > 0 and not self._cells[i - 1][j].visited:
                neighbors.append(('left', i - 1, j))
            if i < self._cols - 1 and not self._cells[i + 1][j].visited:
                neighbors.append(('right', i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                neighbors.append(('up', i, j - 1))
            if j < self._rows - 1 and not self._cells[i][j + 1].visited:
                neighbors.append(('down', i, j + 1))

            if not neighbors:
                self._draw_cell(i, j)
                return

            direction, ni, nj = random.choice(neighbors)
            neighbor = self._cells[ni][nj]

            if direction == 'left':
                current.has_left_wall = False
                neighbor.has_right_wall = False
            elif direction == 'right':
                current.has_right_wall = False
                neighbor.has_left_wall = False
            elif direction == 'up':
                current.has_top_wall = False
                neighbor.has_bottom_wall = False
            elif direction == 'down':
                current.has_bottom_wall = False
                neighbor.has_top_wall = False

            self._draw_cell(i, j)
            self._draw_cell(ni, nj)

            self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        current.highlight("yellow")
        self._animate()

        if i == self._cols - 1 and j == self._rows - 1:
            return True
        
        directions = [
            ('left', i - 1, j, current.has_left_wall),
            ('right', i + 1, j, current.has_right_wall),
            ('up', i, j - 1, current.has_top_wall),
            ('down', i, j + 1, current.has_bottom_wall),
        ]

        for direction, ni, nj, has_wall in directions:
            if 0 <= ni < self._cols and 0 <= nj < self._rows:
                neighbor = self._cells[ni][nj]
                if not has_wall and not neighbor.visited:
                    current.draw_move(neighbor, undo=False)
                    if self._solve_r(ni, nj):
                        return True
                    current.draw_move(neighbor, undo=True)

        current.highlight("#d9d9d9")
        self._animate()

        return False