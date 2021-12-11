#!/usr/bin/env python
"""FizzBuzz implementation."""

from typing import Optional

_KEYWORD_MAPPING = {
    3: "Fizz",
    5: "Buzz",
}


def fizzbuzz(number: int, keyword_mapping: Optional[dict] = None):
    """Run FizzBuzz against a number.

    Prints a number, except where printing each keyword mapped to
    divisible keys in a dictionary.

    Args:
        number (int): FizzBuzz will run against this integer.
        keyword_mapping (dict|None): Number -> keyword mapping.

    Returns:
        None
    """
    if keyword_mapping is None:
        keyword_mapping = _KEYWORD_MAPPING

    output = ""

    for key in keyword_mapping:
        if number % key == 0:
            output += keyword_mapping[key]

    if not output:
        output = str(number)

    return output


def fizzbuzz_range(
    number_limit: int, keyword_mapping: Optional[dict] = None
) -> None:
    """Run FizzBuzz against a number range.

    Print integers 1 to n, except where printing each keyword mapped to
    divisible keys in a dictionary.

    Args:
        number_limit (int): FizzBuzz will run from 1 to this integer.
        keyword_mapping (dict|None): Number -> keyword mapping.

    Returns:
        None
    """
    if keyword_mapping is None:
        keyword_mapping = _KEYWORD_MAPPING

    for number in range(1, number_limit + 1):
        print(fizzbuzz(number, keyword_mapping))

    return None
