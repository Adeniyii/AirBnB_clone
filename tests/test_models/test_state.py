#!/usr/bin/python3
"""Unit tests for the `state` module.
"""
import unittest
from models.state import State

s1 = State()

class TestState(unittest.TestCase):
    """Test cases for the `State` class."""

    def test_params(self):
        self.assertEqual(s1.name, "")
        s1.name = "Abuja"
        self.assertEqual(s1.name, "Abuja")

if __name__ == "__main__":
	unittest.main()


