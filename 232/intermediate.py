#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Daily Programmer #232, Intermediate: Where Should Grandma's House Go?
# https://redd.it/3l61vx

from math import sqrt
import sys
from typing import List, Tuple


class House(object):
    """A house, with Cartesian coordinates."""

    def __init__(self, x: float, y: float):
        """Create a house object with the given coordinates."""
        self.x = x
        self.y = y

    def __matmul__(self, other) -> float:
        """Check the distance between two houses.

        I used __matmul__ for this because it has the nice-looking "@" operator.
        """
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self) -> str:
        return '(%s, %s)' % (self.x, self.y)


class Neighbourhood(object):
    """A neighbourhood of houses."""

    def __init__(self, houses: List[House]):
        self.houses = houses

    def get_closest(self) -> Tuple[House, House]:
        """Find the two closest houses."""
        shortest_distance = self.houses[-1] @ self.houses[-2]
        closest_houses = (self.houses[-2], self.houses[-1])
        for i in range(len(self.houses) - 2):
            for j in range(i+1, len(self.houses) - 1):
                distance = self.houses[i] @ self.houses[j]
                if distance < shortest_distance:
                    shortest_distance = distance
                    closest_houses = (self.houses[i], self.houses[j])
        return closest_houses

    @classmethod
    def make_neighbourhood(cls, locations: List[str]) -> List:
        """Make a list of houses from a list of location strings.

        Each string should look as follows:
        '(0.0000000000, 1.1111111)'
        The zeroes represent the X coordinate and the ones represent Y.
        """
        houses = []
        for house in locations:
            x, y = house.strip('()\n').split(',')
            houses.append(House(float(x), float(y)))
        return cls(houses)


def main():
    file = open(sys.argv[1])
    while True:
        try:
            num_houses = int(file.readline())
        except ValueError:
            break
        houses = []
        for _ in range(num_houses):
            houses.append(file.readline())
        neighbourhood = Neighbourhood.make_neighbourhood(houses)
        closest = neighbourhood.get_closest()

        print('%s %s' % closest)
    file.close()

if __name__ == '__main__':
    main()
