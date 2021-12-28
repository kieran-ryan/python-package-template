"""Library top-level unit tests."""

import unittest

import python_library_template


class TestLibrary(unittest.TestCase):
    """Test library top-level."""

    def test_all_contains_version(self):
        """Library top-level contains version information."""
        self.assertTrue("__version__" in python_library_template.__all__)
