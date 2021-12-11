#!/usr/bin/env python
"""FizzBuzz implementation."""

from typing import Optional

_KEYWORD_MAPPING = {
    3: "Fizz",
    5: "Buzz",
}


def run(number_limit: int, keyword_mapping: Optional[dict] = None) -> None:
    """Run FizzBuzz against a number range.

    Print integers 1 to n, except where printing each keyword mapped to
    divisible keys in a dictionary.

    Args:
        number_limit (int): FizzBuzz will be run from 1 to this integer.
        keyword_mapping (dict|None): Number -> keyword mapping.

    Returns:
        None
    """
    if keyword_mapping is None:
        keyword_mapping = _KEYWORD_MAPPING

    for number in range(1, number_limit + 1):
        output = ""

        for key in keyword_mapping:
            if number % key == 0:
                output += keyword_mapping[key]

        if not output:
            output = str(number)

        print(output)

    return None
