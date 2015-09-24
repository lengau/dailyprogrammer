#!/usr/bin/env python3
# Daily Programmer #233, Easy: The House that ASCII Built
# https://redd.it/3ltee2

from itertools import product
import random
from typing import List

TESTS = [
    [
        '   *',
        '  ***',
        '*******',
    ],
    [
        ' *',
        '***',
        '***',
        '***',
        '***',
        '***',
        '***',
    ],[
        '    **',
        '*** **',
        '******',
    ],[
        '***                    ***',
        '***     **  ***  **    ***',
        '***   ***************  ***',
        '***   ***************  ***',
        '***   ***************  ***',
        '**************************',
        '**************************',
    ]
]


class Castle(object):
    """A castle facade."""

    def __init__(self, rows: List[str]):
        self.blueprint = rows
        self.width = 1 + 4 * len(rows[-1])
        self.height = 1 + 2 * len(rows)
        self.roof_height = 2 * max(len(roof) for roof in rows[0].split())
        self.drawn = False
        self.drawn_shadow = False

    def make_canvas(self):
        self.shadow = [[' ' for _ in range(self.width)] for _ in range(self.height + self.roof_height)]
        self.canvas = [[' ' for _ in range(self.width)] for _ in range(self.height + self.roof_height)]
        self.drawn = False
        self.drawn_shadow = False

    def draw_shadow(self):
        for y, row in enumerate(reversed(self.blueprint)):
            for x, box in enumerate(row):
                if not box.isspace():
                    canvas_x = x * 4
                    canvas_y = y * 2
                    for dx, dy in product(range(5), range(3)):
                        self.shadow[canvas_y + dy][canvas_x + dx] = '*'
        self.drawn_shadow = True

    def __str__(self):
        return '\n'.join(''.join(row) for row in reversed(self.canvas))

    def _outside_neighbours(self, x: int, y: int):
        """Count the number of neighbours that are outside the house."""
        neighbours_outside = 0
        for dy, dx in product((-1, 0, 1), repeat=2):
            if y + dy < 0 or y + dy >= self.height or x + dx < 0 or x + dx >= self.width:
                neighbours_outside += 1
            else:
                location = self.shadow[y + dy][x + dx]
                neighbours_outside += 1 if location.isspace() else 0
        return neighbours_outside

    def is_corner(self, x: int, y: int):
        """Determine if the specified coordinate is a corner."""
        return self._outside_neighbours(x, y) in (1, 5)

    def is_edge(self, x: int, y: int):
        """Determine if the specified coordinate is on an edge."""
        return self._outside_neighbours(x, y) in (2, 3)

    def is_roof(self, x: int, y: int):
        """Return whether the specified coordinate is a roof."""
        return self.is_edge(x, y) and self.shadow[y + 1][x].isspace()

    def draw_building(self, fill=' '):
        """Draw the ASCII house/castle."""
        for x, y in product(range(self.width), range(self.height)):
            if self.shadow[y][x].isspace():
                continue
            if self.is_corner(x, y):
                self.canvas[y][x] = '+'
            elif self.is_edge(x, y):
                if self.is_roof(x, y) or y == 0:
                    self.canvas[y][x] = '—'
                else:
                    self.canvas[y][x] = '|'
            else:
                if not fill.isspace():
                    self.canvas[y][x] = fill

    def draw_doors(self, door='|‾|'):
        """Add the door in the appropriate spot.

        Despite the specification saying the door should be in a random spot,
        I decided instead to place the doors in the middle of the tallest
        towers. The number of doors corresponds 1:1 with the number of
        towers.
        """
        door_towers = self.blueprint[0].split()
        last_index = 0
        for tower in door_towers:
            tower_start = 4 * self.blueprint[0].index(tower, last_index) + 1
            last_index = self.blueprint[0].index(tower, last_index) + 1
            tower_width = len(tower) * 4 - 1
            tower_centre = tower_start + tower_width / 2
            door_start = int(tower_centre - len(door) / 2)
            for i, char in enumerate(door):
                self.canvas[1][door_start + i] = char

    def draw_roof(self, roof_left='/', roof_right='\\', roof_top='A', towers_only=False):
        """Add pointed roofs."""
        roofs = []  # Contains tuples of (y, x_start, x_end)
        last_height = -1
        for x, y in product(range(self.width), range(self.height)):
            if self.is_roof(x, y):
                if y == last_height:
                    roofs[-1] = (roofs[-1][0], roofs[-1][1], x)
                else:
                    roofs.append((y, x))
                last_height = y
        if towers_only:
            tower_roofs = []
            for i, roof in enumerate(roofs):
                if i == len(roofs) - 1:
                    if roofs[i-1][0] < roof[0]:
                        tower_roofs.append(roof)
                elif i == 0:
                    if roofs[1][0] < roof[0]:
                        tower_roofs.append(roof)
                elif roofs[i-1][0] < roof[0] and roofs[i+1][0] < roof[0]:
                    tower_roofs.append(roof)
            roofs = tower_roofs
        for y, x_start, x_end in roofs:
            middle = (x_end - x_start) // 2
            for dx in range(middle):
                self.canvas[y + dx + 1][x_start + dx] = roof_left
                self.canvas[y + dx + 1][x_end - dx] = roof_right
            self.canvas[y + middle + 1][x_start + middle] = roof_top

    def draw_windows(self, window='□'):
        """Randomly draw some windows on the house."""
        for x, y in product(range(len(self.blueprint[-1])),
                            range(len(self.blueprint))):
            try:
                if self.blueprint[len(self.blueprint) - y - 1][x].isspace():
                    continue
            except IndexError:
                continue
            if random.randint(0, 2):
                continue
            canvas_x = 4 * x + 1
            canvas_y = 2 * y + 1
            if ''.join(self.canvas[canvas_y][canvas_x:canvas_x + 3]).isspace():
                self.canvas[canvas_y][canvas_x + 1] = window

def main():
    for test in TESTS:
        c = Castle(test)
        c.make_canvas()
        c.draw_shadow()
        c.draw_building()
        c.draw_doors()
        c.draw_roof()
        c.draw_windows()
        print(c)

if __name__ == '__main__':
    main()
