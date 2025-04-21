from line import Line
from point import Point

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self._win = win

    def draw(self):
        wall_color = "black"
        bg_color = "#d9d9d9"

        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), wall_color
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), bg_color
            )

        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), wall_color
            )
        else:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), bg_color
            )

        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y2), Point(self._x1, self._y2)), wall_color
            )
        else:
            self._win.draw_line(
                Line(Point(self._x2, self._y2), Point(self._x1, self._y2)), bg_color
            )

        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x1, self._y1)), wall_color
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x1, self._y1)), bg_color
            )

    def draw_move(self, to_cell, undo=False):
        from_x = (self._x1 + self._x2) // 2
        from_y = (self._y1 + self._y2) // 2
        to_x = (to_cell._x1 + to_cell._x2) // 2
        to_y = (to_cell._y1 + to_cell._y2) // 2

        color = "gray" if undo else "red"

        self._win.draw_line(Line(Point(from_x, from_y), Point(to_x, to_y)), color)

    def highlight(self, color):
        x1 = self._x1 + 2
        y1 = self._y1 + 2
        x2 = self._x2 - 2
        y2 = self._y2 - 2

        self._win.canvas().create_rectangle(
            x1, y1, x2, y2,
            fill=color,
            outline=color
        )
        self._win.redraw()