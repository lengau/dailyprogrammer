#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Generate a bunch of random points into a text file.

import random
import sys

number_of_points = int(sys.argv[1])
filename = sys.argv[2]

file = open(filename, 'w+')
file.write('%d\n' % (number_of_points))

for _ in range(number_of_points):
    file.write('(%.10f,%.10f)\n' % (random.uniform(-10, 10), random.uniform(-10, 10)))
