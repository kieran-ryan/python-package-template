"""FizzBuzz implementation."""

from __future__ import annotations

import collections

# Order will reflect output e.g. swapping values will result in
# BuzzFizz on common dividends.
_KEYWORD_MAPPING: dict[int, str] = collections.OrderedDict(
    {
        3: "Fizz",
        5: "Buzz",
    },
)


def fizzbuzz(number: int | float, keyword_mapping: dict[int, str] | None = None) -> str:
    """Run FizzBuzz against a number.

    Returns a number, except where returning each keyword mapped to
    divisible keys in a dictionary.

    Args:
        number: Number FizzBuzz will run against.
        keyword_mapping: FizzBuzz keyword mapping.

    Returns:
        Number, or keyword if mapped to a divisible dictionary key.

    Examples:
        >>> fizzbuzz(3)
        'Fizz'
        >>> fizzbuzz(4)
        '4'
        >>> fizzbuzz(5)
        'Buzz'
        >>> fizzbuzz(15)
        'FizzBuzz'
        >>> fizzbuzz(7, {7: "Riff"})
        'Riff'
    """
    keywords = keyword_mapping or _KEYWORD_MAPPING

    output = "".join(keywords[key] for key in keywords if number % key == 0)

    return output or str(number)
