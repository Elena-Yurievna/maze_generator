import unittest
from unittest.mock import Mock
from maze import Maze
from cell import Cell

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.x1 = 50
        self.y1 = 50
        self.num_rows = 5
        self.num_cols = 5
        self.cell_size_x = 50
        self.cell_size_y = 50

        self.win = Mock()
        self.win.redraw = Mock()

        self.maze = Maze(
            x1=self.x1,
            y1=self.y1,
            num_rows=self.num_rows,
            num_cols=self.num_cols,
            cell_size_x=self.cell_size_x,
            cell_size_y=self.cell_size_y,
            win=self.win
        )
    
    def test_initialization(self):
        self.assertEqual(self.maze._x1, self.x1)
        self.assertEqual(self.maze._y1, self.y1)
        self.assertEqual(self.maze._rows, self.num_rows)
        self.assertEqual(self.maze._cols, self.num_cols)
        self.assertEqual(self.maze._cell_width, self.cell_size_x)
        self.assertEqual(self.maze._cell_height, self.cell_size_y)
        self.assertEqual(len(self.maze._cells), self.num_cols)
        self.assertEqual(len(self.maze._cells[0]), self.num_rows)
    
    def test_create_cells(self):
        self.assertEqual(len(self.maze._cells), self.num_cols)
        for column in self.maze._cells:
            self.assertEqual(len(column), self.num_rows)
            for cell in column:
                self.assertIsInstance(cell, Cell)
    
    def test_draw_cell(self):
        cell = self.maze._cells[0][0]
        self.assertEqual(cell._x1, self.x1)
        self.assertEqual(cell._y1, self.y1)
        self.assertEqual(cell._x2, self.x1 + self.cell_size_x)
        self.assertEqual(cell._y2, self.y1 + self.cell_size_y)

    def test_animate(self):
        self.win.redraw.reset_mock()
        self.maze._animate()
        self.win.redraw.assert_called_once()

    def test_break_entrance_and_exit(self):
        entrance = self.maze._cells[0][0]
        exit_cell = self.maze._cells[self.maze._cols - 1][self.maze._rows - 1]

        self.assertFalse(entrance.has_top_wall, "Entrance top wall should be removed")
        self.assertFalse(exit_cell.has_bottom_wall, "Exit bottom wall should be removed")

    def test_reset_cells_visited(self):
        for column in self.maze._cells:
            for cell in column:
                cell.visited = True

        self.maze._reset_cells_visited()

        for column in self.maze._cells:
            for cell in column:
                self.assertFalse(cell.visited, "Cell.visited should be reset to False")


if __name__ == '__main__':
    unittest.main()