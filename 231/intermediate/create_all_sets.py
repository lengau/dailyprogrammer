#!/usr/bin/python3
# Create all possible sets for Set.

shapes = 'DOS'
colours = 'RPG'
numbers = '123'
shades = 'OHF'

for shape in shapes:
    for colour in colours:
        for number in numbers:
            for shade in shades:
                print('{0}{1}{2}{3}'.format(shape, colour, number, shade))
