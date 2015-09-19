#!/usr/bin/env python3
# Daily Programmer #231, easy edition: Cellular Automata Rule 90
# https://redd.it/3jz8tt

import sys

DEFAULT_STARTING_STATES = [
    '1101010',
    '0' * 49 + '1' + '0' * 49,
]

class Cell(object):
    """A single cell for use in cellular automata."""

    def __init__(self, state: bool):
        self.state = state
        self.neighbours = ()

    def __xor__(self, other) -> bool:
        return self.state ^ other.state

    def calculate_step(self):
        self.next_state = False
        for neighbour in self.neighbours:
            self.next_state = self.next_state ^ neighbour.state

    def take_step(self):
        self.state = self.next_state
        del self.next_state

    def __str__(self) -> str:
        return 'x' if self.state else '_'

    def __or__(self, other) -> bool:
        return self.state | other


def main():
    starting_states = sys.argv[1:]
    if starting_states == []:
        starting_states = DEFAULT_STARTING_STATES
    for state in starting_states:
        cells = []
        for cell in state:
            cells.append(Cell(bool(int(cell))))

        cells[0].neighbours = (cells[1],)
        for i in range(1, len(cells) - 1):
            cells[i].neighbours = (cells[i-1], cells[i+1])
        cells[-1].neighbours = (cells[-2],)

        # Simulation
        for step in range(26):
            print(''.join(str(cell) for cell in cells))
            print('')
            for cell in cells:
                cell.calculate_step()
            for cell in cells:
                cell.take_step()
            living_cells = False
            for cell in cells:
                living_cells = cell | living_cells
            if not living_cells:
                break

if __name__ == '__main__':
    main()
