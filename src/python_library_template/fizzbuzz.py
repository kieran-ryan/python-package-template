"""FizzBuzz implementation."""
from typing import Optional

_KEYWORD_MAPPING = {
    3: "Fizz",
    5: "Buzz",
}


def fizzbuzz(
    number: int | float, keyword_mapping: Optional[dict] = None
) -> str:
    """Run FizzBuzz against a number.

    Returns a number, except where returning each keyword mapped to
    divisible keys in a dictionary.

    Args:
        number (int | float): Number FizzBuzz will run against.
        keyword_mapping (Optional[dict]): Number -> keyword mapping.

    Returns:
        str: Number, or keyword if mapped to divisible dictionary key.
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
