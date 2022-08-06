#!/usr/bin/python3
"""Unit tests for the `state` module.
"""
import unittest
from models.state import State
from models import storage
from datetime import datetime

s1 = State()
a2 = State(**a1.to_dict())
a3 = State("hello", "wait", "in")

class TestState(unittest.TestCase):
    """Test cases for the `State` class."""

    def test_params(self):
        self.assertIsInstance(s1.name, str)
        s1.name = "Chicago"
        self.assertEqual(s1.name, "Chicago")

if __name__ == "__main__":
	unittest.main()


