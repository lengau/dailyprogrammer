#!/usr/bin/env python3
# Daily Programmer #213, hard edition: Stepstring Discrepancy
# http://redd.it/358pfk

import sys
import timeit

# Make this run with both python2 and python3.
try:
	xrange(0)
except NameError:
	xrange = range

"""
The next three functions form my original attempt to solve this problem.
They were written to make sure I understood the problem, and although they do
technically solve it, they should not be considered anything but an
intermediate product.
"""


def discrepancy(string, first='a', second='b'):
	"""Finds the discrepancy of an input string.

	The input string is assumed to contain only two types of character."""
	amounts = {
		first: 0,
		second: 0
	}
	for character in string:
		amounts[character] += 1
	return abs(amounts['a'] - amounts['b'])


def stepstrings(string):
	"""A generator that yields every possible substring of a string."""
	for start in xrange(len(string)):
		yield string[start]
		for end in xrange(start+1, len(string)):
			#yield string[start:end]
			for step in xrange(1, end-start+1):
				if (end - start) % step == 0:
					yield string[start:end+1:step]


def slow_stepstring_discrepancy(string):
	"""Finds the largest stepstring discrepancy of the input string.
	>>> slow_stepstring_discrepancy(
	...  'bbaaabababbaabbaaaabbbababbaabbbaabbaaaaabbababaaaabaabbbaaa')
	9
	>>> slow_stepstring_discrepancy(
	...  'bbaaaababbbaababbbbabbabababababaaababbbbbbaabbaababaaaabaaa')
	12
	>>> slow_stepstring_discrepancy(
	...  'aaaababbabbaabbaabbbbbbabbbaaabbaabaabaabbbaabababbabbbbaabb')
	11
	>>> slow_stepstring_discrepancy(
	...  'abbabbbbbababaabaaababbbbaababbabbbabbbbaabbabbaaabbaabbbbbb')
	15
	"""
	biggest_discrepancy = 0
	for stepstring in stepstrings(string):
		new_discrepancy = discrepancy(stepstring)
		if new_discrepancy > biggest_discrepancy:
			biggest_discrepancy = new_discrepancy
	return biggest_discrepancy

"""
The following two functions form my actual solution to this problem. They can
still be optimised, but I consider them to be good enough at this point since
my computer completes execution with a 10,000 character string in under 10
seconds.

Potential routes for later optimization include:
 * full_length_stepstrings could yield an iterator that either returns the
   character from string or returns an index of str to use. It would also need
   to yield the length of the stepstring that iterator represents in order for
   fast_stepstring_discrepancy to function as is.
 * fast_stepstring_discrepancy could use multiprocess to check stepstrings
   in parallel. In fact, for long enough strings, it may be worthwhile to
   consider distributed computing efforts. Each client may receieve the entire
   string and a set of stepstring iterators. It would perform the contents of
   fast_stepstring_discrepancy with minor adjustments and then return the
   maximum discrepancy it finds to the host.
"""
def full_length_stepstrings(string):
	for step_length in range(len(string)-1):
		for start in range(step_length):
			yield string[start::step_length]

def fast_stepstring_discrepancy(string, plus='a', minus='b'):
	"""Finds the largest stepstring discrepancy of the input string.
	>>> fast_stepstring_discrepancy(
	...  'bbaaabababbaabbaaaabbbababbaabbbaabbaaaaabbababaaaabaabbbaaa')
	9
	>>> fast_stepstring_discrepancy(
	...  'bbaaaababbbaababbbbabbabababababaaababbbbbbaabbaababaaaabaaa')
	12
	>>> fast_stepstring_discrepancy(
	...  'aaaababbabbaabbaabbbbbbabbbaaabbaabaabaabbbaabababbabbbbaabb')
	11
	>>> fast_stepstring_discrepancy(
	...  'abbabbbbbababaabaaababbbbaababbabbbabbbbaabbabbaaabbaabbbbbb')
	15
	"""
	max_disc = 0
	for stepstring in full_length_stepstrings(string):
		if len(stepstring) < max_disc:
			continue
		for start in range(len(stepstring)-max_disc):
			discrepancy = 0
			for index in range(start, len(stepstring)):
				if stepstring[index] == plus:
					discrepancy += 1
				elif stepstring[index] == minus:
					discrepancy -= 1
				if abs(discrepancy) > max_disc:
					max_disc = abs(discrepancy)
			if len(stepstring) - start < max_disc:
				break
	return max_disc



if __name__ == '__main__':
	print('Performing tests...')
	import doctest
	doctest.testmod()
	test_input = [
		'bbaaabababbaabbaaaabbbababbaabbbaabbaaaaabbababaaaabaabbbaaa',
		'bbaaaababbbaababbbbabbabababababaaababbbbbbaabbaababaaaabaaa',
		'aaaababbabbaabbaabbbbbbabbbaaabbaabaabaabbbaabababbabbbbaabb',
		'abbabbbbbababaabaaababbbbaababbabbbabbbbaabbabbaaabbaabbbbbb',
	]
	print('Testing speed on the following strings:')
	for line in test_input:
		print(line)
		print('Slow:')
		print(timeit.timeit(
			'slow_stepstring_discrepancy("%s")' % line,
			setup='from __main__ import slow_stepstring_discrepancy', number=100))
		print('Fast:')
		print(timeit.timeit(
			'fast_stepstring_discrepancy("%s")' % line,
			setup='from __main__ import fast_stepstring_discrepancy',
			number=100))
	print('Performing challenge.')
	results = []
	expected_results = [113, 117, 121, 127, 136, 136, 138, 224]
	with open('hard_strings.txt') as f:
		for line in f.readlines():
			results.append(fast_stepstring_discrepancy(line[:-2]))
	if results == expected_results:
		print('Challenge succeeded.')
	else:
		print('Challenge failed')
	print('Achieved results:')
	print(results)
	print('Expected results:')
	print(expected_results)
