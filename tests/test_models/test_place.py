#!/usr/bin/python3
"""Unit tests for the `city` module.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.place import Place
from models import storage
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test cases for the `Place` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        p1 = Place()
        p3 = Place("hello", "wait", "in")
        k = f"{type(p1).__name__}.{p1.id}"
        self.assertIsInstance(p1.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(p3.name, "")

        self.assertIsInstance(p1.name, str)
        self.assertIsInstance(p1.user_id, str)
        self.assertIsInstance(p1.city_id, str)
        self.assertIsInstance(p1.description, str)
        self.assertIsInstance(p1.number_bathrooms, int)
        self.assertIsInstance(p1.number_rooms, int)
        self.assertIsInstance(p1.price_by_night, int)
        self.assertIsInstance(p1.max_guest, int)
        self.assertIsInstance(p1.longitude, float)
        self.assertIsInstance(p1.latitude, float)
        self.assertIsInstance(p1.amenity_ids, list)

    def test_init(self):
        """Test method for public instances"""

        p1 = Place()
        p2 = Place(**p1.to_dict())
        self.assertIsInstance(p1.id, str)
        self.assertIsInstance(p1.created_at, datetime)
        self.assertIsInstance(p1.updated_at, datetime)
        self.assertEqual(p1.updated_at, p2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        p1 = Place()
        string = f"[{type(p1).__name__}] ({p1.id}) {p1.__dict__}"
        self.assertEqual(p1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        p1 = Place()
        old_update = p1.updated_at
        p1.save()
        self.assertNotEqual(p1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        p1 = Place()
        p2 = Place(**p1.to_dict())
        a_dict = p2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(p2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(p1, p2)


if __name__ == "__main__":
    unittest.main()
