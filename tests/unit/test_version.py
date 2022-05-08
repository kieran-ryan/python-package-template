"""Library version unit tests."""

import unittest

import packaging.version

from pysamplelib.__version__ import __version__


class TestVersion(unittest.TestCase):
    """Test `version.py` contains a valid `__version__`."""

    def test_version_is_valid(self):
        """Library version is valid."""
        parsed_version = packaging.version.parse(__version__)
        self.assertTrue(isinstance(parsed_version, packaging.version.Version))
        self.assertTrue(isinstance(parsed_version.major, int))
        self.assertTrue(isinstance(parsed_version.minor, int))
        self.assertTrue(isinstance(parsed_version.micro, int))
