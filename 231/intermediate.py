#!/usr/bin/env python3
# Daily Programmer #231, intermediate edition: Set Game Solver
# https://redd.it/3ke4l6

from enum import Enum
import sys

class Shape(Enum):
    diamond = 'D'
    oval = 'O'
    squiggle = 'S'

class Colour(Enum):
    red = 'R'
    purple = 'P'
    green = 'G'

class Shading(Enum):
    open = 'O'
    hatched = 'H'
    filled = 'F'

class Card(object):
    """A card for a Set game."""

    def __init__(self, shape: Shape, colour: Colour,
                 shading: Shading, number: int):
        if 1 <= number <= 3:
            self.number = number
        else:
            raise ValueError('Invalid number of shapes')
        self.shape = shape
        self.colour = colour
        self.shading = shading

    @classmethod
    def is_set(cls, *cards) -> bool:
        """Check if three cards make a set."""
        if len(cards) != 3:
            raise ValueError('Wrong number of cards given. Expected 3.')
        # TODO: Don't repeat this if statement.
        if len(set(card.shape for card in cards)) not in (1, 3):
            return False
        if len(set(card.colour for card in cards)) not in (1, 3):
            return False
        if len(set(card.shading for card in cards)) not in (1, 3):
            return False
        if len(set(card.number for card in cards)) not in (1, 3):
            return False
        return True

    def __str__(self) -> str:
        aspect_strings = [
            aspect.name[0] for aspect in (
                self.shape, self.colour, self.shading)] + [self.number]
        return '{0}{1}{3}{2}'.format(*aspect_strings).upper()

    @classmethod
    def from_string(cls, string: str):
        shape = Shape(string[0])
        colour = Colour(string[1])
        number = int(string[2])
        shading = Shading(string[3])
        return cls(shape=shape, colour=colour, number=number, shading=shading)


def main():
    cards = []
    with open(sys.argv[1]) as file:
        for line in file.readlines():
            cards.append(Card.from_string(line))

    if len(sys.argv) > 2:
        expected = set()
        with open(sys.argv[2]) as file:
            for line in file.readlines():
                expected.add(line)

    output = set()
    for first, second, third in generate_sets(cards):
        output.add('%s %s %s\n' % (first, second, third))

    if len(sys.argv) > 2:
        print('Expected:')
        for line in expected:
            print(line, end='')

    print('Output:')
    for line in output:
        print(line, end='')

    if len(sys.argv) > 2:
        try:
            assert output == expected
        except AssertionError:
            print('Test failed.')
        else:
            print('Test passed.')

def generate_sets(cards):
    for i in range(len(cards) - 2):
        for j in range(i+1, len(cards) - 1):
            for k in range(j+1, len(cards)):
                if Card.is_set(cards[i], cards[j], cards[k]):
                    yield cards[i], cards[j], cards[k]

if __name__ == '__main__':
    main()
