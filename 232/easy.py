#!/usr/bin/env python3
# Daily Programmer #232, easy edition: Palindromes
# https://redd.it/3kx6oh
"""
DailyProgrammer # 232: Palindromes.

See the Daily Programmer link above for information on this challenge.

I'm going to start writing these with Python 3.5 type hints. I'll be using mypy
to type check them.
"""

import os
import string
from typing import List, TextIO, Union

TEST_ANSWERS = [True, False, False, True, True, True]


class Palindrome:
    """A potential palindrome.

    Please note that this could use some further improvement if it were to be
    used in a large capacity. For example, is_palindrome should check more
    efficiently. Perhaps start at the beginning and end of the string and
    check one character at a time. Even better would be to do that in a C
    module to do so.
    """

    def __init__(self, candidate: Union[str, List[str]]):
        """Create a palindrome object from a list of strings."""
        self.candidate = ''.join(candidate)
        self.__make_alphabetical()

    def __make_alphabetical(self) -> None:
        """Strip everything but letters and make lowercase.."""
        self.candidate = ''.join(
            [i for i in self.candidate if i in string.ascii_letters])
        self.candidate = self.candidate.lower()

    def is_palindrome(self) -> bool:
        """Is this string actually a palindrome?"""
        return self.candidate == self.candidate[::-1]

    @classmethod
    def create_from_file(cls, file: TextIO) -> List:
        """Create a list of palindrome objects from a file object."""
        current_location = file.tell()
        file.seek(0, os.SEEK_END)
        file_length = file.tell()
        file.seek(current_location)

        palindromes = []  # type: List[Palindrome]
        while file.tell() < file_length:
            try:
                palindrome_length = int(file.readline())
            except ValueError as e:
                raise ValueError('Malformed file') from e
            palindrome = []
            for _ in range(palindrome_length):
                palindrome.append(file.readline())
            palindromes.append(cls(palindrome))
        return palindromes


def test():
    """Test the Naive palindrome checker implementation."""
    with open('easy/test_inputs.txt') as inputs:
        palindromes = Palindrome.create_from_file(inputs)
    for palindrome in palindromes:
        pass # print('Palindrome' if palindrome.is_palindrome() else 'Not a palindrome')
    answers = [p.is_palindrome() for p in palindromes]
    assert answers == TEST_ANSWERS


if __name__ == '__main__':
    test()
