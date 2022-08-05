#!/usr/bin/python3
"""Unit tests for the `amenity` module.
"""
import unittest
from models.amenity import Amenity

a1 = Amenity()

class TestAmenity(unittest.TestCase):
    """Test cases for the `Amenity` class."""

    def test_params(self):
        """"""
        self.assertEqual(a1.name, "")
        a1.name = "room service"
        self.assertEqual(a1.name, "room service")

if __name__ == "__main__":
	unittest.main()

