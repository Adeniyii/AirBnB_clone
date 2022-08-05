#!/usr/bin/python3
"""Unit tests for the `city` module.
"""
import unittest
from models.city import City

c1 = City()

class TestCity(unittest.TestCase):
    """Test cases for the `City` class."""

    def test_params(self):
        """"""
        self.assertEqual(c1.name, "")
        self.assertEqual(c1.state_id, "")
        c1.name = "Abuja"
        c1.state_id = "seven"
        self.assertEqual(c1.name, "Abuja")
        self.assertEqual(c1.state_id, "seven")

if __name__ == "__main__":
	unittest.main()
