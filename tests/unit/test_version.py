"""Package version unit tests."""

from __future__ import annotations

import unittest

import packaging.version

from pysamplelib.__version__ import __version__


class TestVersion(unittest.TestCase):
    """Test `version.py` contains a valid `__version__`."""

    def test_version_is_valid(self):
        """Package version is valid."""
        parsed_version = packaging.version.parse(__version__)
        assert isinstance(parsed_version, packaging.version.Version)
        assert isinstance(parsed_version.major, int)
        assert isinstance(parsed_version.minor, int)
        assert isinstance(parsed_version.micro, int)
