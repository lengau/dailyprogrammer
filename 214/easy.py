#!/usr/bin/env python3
# Daily Programmer #214, easy edition: Calculating the standard deviation
# http://redd.it/35l5eo

from __future__ import (division, print_function)
try:
	from builtins import input
except ImportError:
	input = raw_input


def std_dev(population):
	"""Calculates the standard deviation of a population.
	>>> std_dev([5, 6, 11, 13, 19, 20, 25, 26, 28, 37,])
	9.7775
	>>> std_dev(
	...  [37, 81, 86, 91, 97, 108, 109, 112, 112, 114, 115, 117, 121, 123, 141])
	23.2908
	"""
	mean = sum(population)/len(population)
	variance = 0
	for item in population:
		variance += (item - mean)**2
	variance /= len(population)
	return round(variance**0.5, 4)


def std_dev_input(population_string=None):
	"""Calculates the standard deviation of a population input as a string.
	>>> std_dev_input('5 6 11 13 19 20 25 26 28 37')
	9.7775
	>>> std_dev_input('37 81 86 91 97 108 109 112 112 114 115 117 121 123 141')
	23.2908
	"""
	if population_string is None:
		population_string = input('Population: ')
	population = tuple(map(int, population_string.split()))
	return std_dev(population)


if __name__ == '__main__':
	import doctest
	doctest.testmod()
	challenge_inputs = (
		'266 344 375 399 409 433 436 440 449 476 502 504 530 584 587',
		'809 816 833 849 851 961 976 1009 1069 1125 1161 1172 1178 '
			'1187 1208 1215 1229 1241 1260 1373',
		)
	for challenge in challenge_inputs:
		print(std_dev_input(challenge))
