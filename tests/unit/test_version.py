"""Library version unittests."""
import unittest

from packaging import version
from version import __version__


class TestVersion(unittest.TestCase):
    """Test `version.py` contains a valid `__version__`."""

    def test_version_is_valid(self):
        """Library version is valid."""
        parsed_version = version.parse(__version__)
        assert isinstance(parsed_version, version.Version)
        assert isinstance(parsed_version.major, int)
        assert isinstance(parsed_version.minor, int)
        assert isinstance(parsed_version.micro, int)
