import os

import numpy as np

from direction import Direction


class GridWalker:
    def __init__(self):
        self.width: int = 15
        self.height: int = 15
        self.x: int = self.width // 2
        self.y: int = self.height // 2
        self.portal_symbol = '@'
        self.player_symbol = '&'
        self.explored_symbol = '.'
        self.unexplored_symbol = '#'
        self.explored_grid: np.ndarray = np.full([self.height, self.width], fill_value=self.unexplored_symbol)
        self.explored_grid[self.y, self.x] = self.portal_symbol

    def print_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print_grid = self.explored_grid.copy()
        print_grid[self.y, self.x] = self.player_symbol
        for row in print_grid:
            for cell in row:
                print(cell, end='')
            print('')

    def move_and_print(self, direction: Direction):
        if direction == Direction.UP:
            self.y -= 1
        elif direction == Direction.DOWN:
            self.y += 1
        elif direction == Direction.RIGHT:
            self.x += 1
        elif direction == Direction.LEFT:
            self.x -= 1
        if self.explored_grid[self.y, self.x] == self.unexplored_symbol:
            self.explored_grid[self.y, self.x] = self.explored_symbol
        self.print_grid()
