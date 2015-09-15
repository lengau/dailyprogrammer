#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Daily Programmer idea: write your own toString() and toInteger()
# https://redd.it/3ihx7o

from typing import Union

DIGIT_STRINGS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z']

"""Be careful with the delimiters variable. After the full stop (.) character,
there are two different types of thin space, which some text editors show in
one column."""
DELIMITERS = ' ,.  '
THOUSANDS_SEPARATOR = ' '
NEGATIVE = '−'
NEGATIVE_INPUTS = '−-－'
POSITIVE = ''
DECIMAL_MARKER = '.'

def to_string(number: int, base: int = 10,
              delimiter: str = THOUSANDS_SEPARATOR,
              delimiter_digits: int = 3) -> str:
    """Turn a number into a string."""
    if base < 2:
        raise ValueError('Arabic numerals only work in base 2 or higher.')
    if base > len(DIGIT_STRINGS):
        raise NotImplementedError(
            'Not enough digits specified in DIGIT_STRINGS')
    if number < 0:
        prefix = NEGATIVE
        number *= -1
    else:
        prefix = ''
    output = ''
    digits = 1
    while number >= base:
        output = DIGIT_STRINGS[number % base] + output
        if digits == delimiter_digits:
            output = delimiter + output
            digits = 1
        else:
            digits += 1
        number = number // base
    return prefix + DIGIT_STRINGS[number] + output

def to_int(number: str, base: int = 10, delimiters: str = DELIMITERS,
           negative_indicators: str = NEGATIVE_INPUTS) -> int:
    """Turn a string into an integer."""
    if number[0] in negative_indicators:
        multiplier = -1
        number = number[1:]
    else:
        multiplier = 1
    output = 0
    number = number[::-1]
    offset = 0
    for i in range(len(number)):
        if number[i] in delimiters:
            offset += 1
            continue
        digit = DIGIT_STRINGS.index(number[i]) * base** (i - offset)
        output += digit
    return multiplier * output

def to_float(number: str, base: int = 10,
             decimal_marker: str = DECIMAL_MARKER, delimiters: str = DELIMITERS,
             negative_indicators: str = NEGATIVE_INPUTS) -> float:
    """Turn a string into a floating point number."""
    if number[0] in negative_indicators:
        multiplier = -1
        number = number[1:]
    else:
        multiplier = 1
    if decimal_marker not in number:
        return float(to_int(number, base=base, delimiters=delimiters))
    try:
        int_part, frac_part = number.split(decimal_marker)
    except ValueError:
        raise ValueError('Too many decimal markers.')
    int_part = to_int(int_part, base=base, delimiters=delimiters)
    frac_part = to_int(frac_part, base=base, delimiters=delimiters)
    while frac_part > 1:
        frac_part /= base
    return multiplier * (int_part + frac_part)

def to_number(number: str,
              base: int = 10,
              decimal_marker: str = DECIMAL_MARKER,
              delimiters: str = DELIMITERS) -> Union[float, int]:
    if decimal_marker in number:
        return to_float(number, base=base, decimal_marker=decimal_marker,
                        delimiters=delimiters)
    return to_int(number, base=base, delimiters=delimiters)

def float_to_string(number: float, base: int = 10, decimals: int = 4,
                    decimal_marker: str = DECIMAL_MARKER,) -> str:
    """Convert a floating point number to a string."""
    int_part = int(number // 1)
    if int_part < 0:
        int_part += 1
    frac_part = number % 1
    if number < 0 and frac_part != 0:
        frac_part = 1 - frac_part
    frac_part *= base ** decimals
    if frac_part % 1 > 0.5:
        frac_part += 1
    frac_part = int(frac_part)
    int_str = to_string(int_part, base=base)
    if number < 0 and int_str == '0':
        int_str = '-0'
    frac_str = to_string(frac_part, base=base, delimiter='')
    try:
        while frac_str[-1] == DIGIT_STRINGS[0]:
            frac_str = frac_str[:-1]
    except IndexError:
        frac_str = '0'
    return int_str + decimal_marker + frac_str
