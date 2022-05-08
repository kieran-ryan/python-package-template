"""FizzBuzz implementation."""

import collections

# Order will reflect output e.g. swapping values will result in
# BuzzFizz on common dividends.
_KEYWORD_MAPPING: dict[int, str] = collections.OrderedDict(
    {
        3: "Fizz",
        5: "Buzz",
    }
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
    if keyword_mapping is None:
        keyword_mapping = _KEYWORD_MAPPING

    output = "".join(
        keyword_mapping[key] for key in keyword_mapping if number % key == 0
    )

    if not output:
        output = str(number)

    return output
