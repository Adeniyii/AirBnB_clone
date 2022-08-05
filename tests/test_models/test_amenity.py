#!/usr/bin/python3
"""Unit tests for the `amenity` module.
"""
import unittest
from models.amenity import Amenity

a1 = Amenity()

class TestAmenity(unittest.TestCase):
    """Test cases for the `Amenity` class."""

    def test_params(self):
        """Test method for class attributes"""
        self.assertIsInstance(a1.name, str)

    def test_init(self):
        """Test method for public instances"""
        self.assertIsInstance(a1.name, str)


if __name__ == "__main__":
	unittest.main()

