"""Package top-level unit tests."""

from __future__ import annotations

import unittest

import pysamplelib


class TestPackage(unittest.TestCase):
    """Test package top-level."""

    def test_all_contains_version(self):
        """Package top-level contains version information."""
        assert "__version__" in pysamplelib.__all__
