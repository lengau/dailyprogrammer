#!/usr/bin/env python3
# Daily Programmer #232, easy edition: Palindromes (BONUS FILE!)
# https://redd.it/3kx6oh
"""Two-word palindromes."""


with open('easy/enable1.txt') as dict_file:
    DICTIONARY = dict_file.read().splitlines()

def generate_palindromes():
    """Generate two-word palindromes from DICTIONARY.

    Note: Because this tries each word pair both ways in one iteration
    rather than iterating over the whole dictionary twice, the word list
    may not be in alphabetical order."""
    for i in range(len(DICTIONARY)):
        for j in range(i+1, len(DICTIONARY)):
            candidate = DICTIONARY[i] + DICTIONARY[j]
            if candidate == candidate[::-1]:
                yield '%s %s' % (DICTIONARY[i], DICTIONARY[j])
            candidate = DICTIONARY[j] + DICTIONARY[i]
            if candidate == candidate[::-1]:
                yield '%s %s' % (DICTIONARY[j], DICTIONARY[i])


if __name__ == '__main__':
    for p in generate_palindromes():
        print(p)
