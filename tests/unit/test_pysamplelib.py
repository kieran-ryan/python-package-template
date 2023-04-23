"""Library top-level unit tests."""

from __future__ import annotations

import unittest

import pysamplelib


class TestLibrary(unittest.TestCase):
    """Test library top-level."""

    def test_all_contains_version(self):
        """Library top-level contains version information."""
        assert "__version__" in pysamplelib.__all__
