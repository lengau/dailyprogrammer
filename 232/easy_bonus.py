#!/usr/bin/env python3
# Daily Programmer #232, easy edition: Palindromes (BONUS FILE!)
# https://redd.it/3kx6oh
"""Two-word palindromes."""

from typing import Union


with open('easy/enable1.txt') as dict_file:
    DICTIONARY = dict_file.read().splitlines()


def palindrome(a:str, b:str) -> Union[str, None]:
    """Generates a palindrome from two words if possible.

    If no palindrome exists, returns None."""
    if a[0] == b[-1] and a[1] == b[-2]:
        candidate = ''.join((a,b))
        if candidate == candidate[::-1]:
            return ' '.join((a,b))


def generate_palindromes():
    """Generate two-word palindromes from DICTIONARY.

    Note: Because this tries each word pair both ways in one iteration
    rather than iterating over the whole dictionary twice, the word list
    may not be in alphabetical order."""
    for i in range(len(DICTIONARY)):
        for j in range(i+1, len(DICTIONARY)):
            candidate = palindrome(DICTIONARY[i], DICTIONARY[j])
            if candidate:
                yield candidate
            candidate = palindrome(DICTIONARY[j], DICTIONARY[i])
            if candidate:
                yield candidate


if __name__ == '__main__':
    for p in generate_palindromes():
        print(p)
