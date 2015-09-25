#!/usr/bin/env python3
# Daily Programmer #233, Intermediate: Conway's Game of Life
# https://redd.it/3m2vvk

from itertools import product
import random
import sys
import time
from typing import List


class Cell(object):
    """A single cell for use in cellular automata."""

    def __init__(self, state: str):
        self.state = state
        self.neighbours = ()
        self.next_state = self.state

    def calculate_step(self):
        if not self.neighbours:
            raise ReferenceError('No neighbours defined')
        alive_neighbours = 0
        for neighbour in self.neighbours:
            if neighbour.state and not neighbour.state.isspace():
                alive_neighbours += 1
        if not self.state or self.state.isspace():
            if alive_neighbours == 3:
                self.next_state = random.choice([
                    n for n in self.neighbours if not n.state.isspace()]).state
            else:
                self.next_state = ' '
            return
        if alive_neighbours not in (2, 3):
            self.next_state = ' '

    def take_step(self):
        self.state = self.next_state

    def __str__(self) -> str:
        return self.state or ' '


def main():
    with open(sys.argv[1]) as file:
        lines = file.read().splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)

    def make_line(width: int, line: str) -> List[Cell]:
        """Make a line of cells."""
        out_line = []
        for cell_state in line:
            out_line.append(Cell(cell_state))
        if len(out_line) < width:
            for _ in range(width - len(out_line)):
                out_line.append(Cell(''))
        return out_line

    grid = []
    for line in lines:
        grid.append(make_line(width, line))

    for y, x in product(range(height), range(width)):
        neighbour_coords = []
        for a, b in product((-1, 0, 1), repeat=2):
            neighbour_coords.append((y+a, x+b))
        neighbour_coords.pop(4)  # The coordinates of the current cell.
        neighbours = []
        for location in neighbour_coords:
            if -1 not in location and location[0] != height and location[1] != width:
                neighbours.append(grid[location[0]][location[1]])
        grid[y][x].neighbours = neighbours

    for i in range(20):
        print("\033c");
        print('Step %d:' % i)
        for line in grid:
            print(''.join(cell.state for cell in line))
        for line in grid:
            for cell in line:
                cell.calculate_step()
        for line in grid:
            for cell in line:
                cell.take_step()
        if ''.join(''.join(cell.state for cell in line) for line in grid).isspace():
            break
        time.sleep(0.75)


if __name__ == '__main__':
    main()
