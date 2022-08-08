#!/usr/bin/python3
"""Unit tests for the `review` module.
"""
import os
import unittest
from models.review import Review
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Test cases for the `Review` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        r1 = Review()
        r3 = Review("hello", "wait", "in")
        k = f"{type(r1).__name__}.{r1.id}"
        self.assertIsInstance(r1.text, str)
        self.assertIsInstance(r1.user_id, str)
        self.assertIsInstance(r1.place_id, str)
        self.assertEqual(r3.text, "")

    def test_init(self):
        """Test method for public instances"""
        r1 = Review()
        r2 = Review(**r1.to_dict())
        self.assertIsInstance(r1.id, str)
        self.assertIsInstance(r1.created_at, datetime)
        self.assertIsInstance(r1.updated_at, datetime)
        self.assertEqual(r1.updated_at, r2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        r1 = Review()
        string = f"[{type(r1).__name__}] ({r1.id}) {r1.__dict__}"
        self.assertEqual(r1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        r1 = Review()
        old_update = r1.updated_at
        r1.save()
        self.assertNotEqual(r1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        r1 = Review()
        r2 = Review(**r1.to_dict())
        a_dict = r2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(r2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
