#!/usr/bin/python3
"""Unit tests for the `amenity` module.
"""
import unittest
from models.amenity import Amenity
from models import storage
from datetime import datetime

a1 = Amenity()
a2 = Amenity(**a1.to_dict())
a3 = Amenity("hello", "wait", "in")

class TestAmenity(unittest.TestCase):
    """Test cases for the `Amenity` class."""

    def test_params(self):
        """Test method for class attributes"""
        k = f"{type(a1).__name__}.{a1.id}"
        self.assertIsInstance(a1.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(a3.name, "")

    def test_init(self):
        """Test method for public instances"""
        self.assertIsInstance(a1.id, str)
        self.assertIsInstance(a1.created_at, datetime)
        self.assertEqual(a1.updated_at, a2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        string = f"[{type(a1).__name__}] ({a1.id}) {a1.__dict__}"
        self.assertEqual(a1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        a1.save()
        self.assertGreater(a1.updated_at, a1.created_at)

    def test_todict(self):
        a_dict = a2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertIn('__class__', a_dict.keys())
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())

if __name__ == "__main__":
	unittest.main()

