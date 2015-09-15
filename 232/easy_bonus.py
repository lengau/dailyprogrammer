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


LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def generate_palindromes_smart():
    """
    Below is a (hopefully) better way to do it. The words are sorted into a pair
    of dictionaries by their first and last letter. Each entry in the dictionaries
    contains the second and penultimate letters. Those inner dictionaries contain
    the words themselves.

    E.g. for the dictionary containing cat, rat, it would be equivalent
    to declaring:
    first_letter = {
        'c': {
            'a': ['cat']
        }
        'r': {
            'a': ['rat']
        }
    }
    last_letter = {
        't': {
            'a': ['cat', 'rat']
        }
    }
    """
    first_letter, last_letter = generate_dictionaries()
    for letter in LETTERS:
        start = first_letter[letter]
        end = last_letter[letter]
        for letter in LETTERS:
            first_words = start[letter]
            last_words = end[letter]
            for first_word in first_words:
                for last_word in last_words:
                    if first_word == last_word:
                        continue
                    candidate = ''.join((first_word, last_word))
                    if candidate == candidate[::-1]:
                        yield ' '.join((first_word, last_word))


def fill_dictionary(dictionaries, constructor):
    for dictionary in dictionaries:
        for letter in LETTERS:
            dictionary[letter] = constructor()


def generate_dictionaries():
    first_letter = {}
    last_letter = {}
    fill_dictionary((first_letter, last_letter), dict)
    fill_dictionary(first_letter.values(), list)
    fill_dictionary(last_letter.values(), list)
    for word in DICTIONARY:
        first_letter[word[0]][word[1]].append(word)
        last_letter[word[-1]][word[-2]].append(word)
    return first_letter, last_letter


if __name__ == '__main__':
    for p in generate_palindromes_smart():
        print(p)
