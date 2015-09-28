#!/usr/bin/env python3
# Daily Programmer #234, Easy: Vampire Numbers
# https://redd.it/3ltee2

from functools import reduce
from itertools import combinations_with_replacement as combine
import operator
import sys

# Inputs are defined by the number of digits required in the vampire and the
# number of fangs to expect.
TEST_INPUT = (4, 2)
CHALLENGE_INPUT = (6, 3)

def generate_vampires(digits, fangs):
    fang_digits = digits // fangs
    fang_start = 10 ** (fang_digits - 1)
    fang_stop = 10 ** fang_digits
    for fangs in combine(range(fang_start, fang_stop), fangs):
        vampire_candidate = reduce(operator.mul, fangs, 1)
        vampire_candidate_digits = sorted(list(str(vampire_candidate)))
        if len(vampire_candidate_digits) != digits:
            continue
        expected_digits = sorted(list(''.join(str(fang) for fang in fangs)))

        if expected_digits == vampire_candidate_digits:
            yield vampire_candidate, fangs


def print_vampires(digits, num_fangs, print_summary=True):
    vampire_list = sorted(generate_vampires(digits, num_fangs))
    i = 0
    last_vampire = 0
    for vampire, fangs in vampire_list:
        if vampire == last_vampire:
            vampire_string = ' ' * len(str(vampire))
        else:
            vampire_string = str(vampire)
            i += 1
        print('%s = %s' % (
            vampire_string, '*'.join(str(fang) for fang in fangs)))
        last_vampire = vampire
    if print_summary:
        print('There are %d vampire numbers with %d digits and %d fangs' % (
            i, digits, num_fangs))


def test():
    print('Test:')
    print_vampires(*TEST_INPUT)

    print('Challenge:')
    print_vampires(*CHALLENGE_INPUT)


def main():
    digits = int(sys.argv[1])
    fangs = int(sys.argv[2])
    print_summary = True
    if len(sys.argv) > 3:
        if sys.argv[3].lower() in ('no', 'false'):
            print_summary = False
    print_vampires(digits, fangs, print_summary)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        test()
    else:
        main()
