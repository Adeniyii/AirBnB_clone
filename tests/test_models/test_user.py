#!/usr/bin/python3
"""Unit tests for the `state` module.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for the `User` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        u1 = User()
        k = f"{type(u1).__name__}.{u1.id}"
        self.assertIn(k, storage.all())
        self.assertIsInstance(u1.email, str)
        self.assertIsInstance(u1.password, str)
        self.assertIsInstance(u1.first_name, str)
        self.assertIsInstance(u1.last_name, str)

    def test_init(self):
        """Test method for public instances"""
        u1 = User()
        u2 = User(**u1.to_dict())
        self.assertIsInstance(u1.id, str)
        self.assertIsInstance(u1.created_at, datetime)
        self.assertIsInstance(u1.updated_at, datetime)
        self.assertEqual(u1.updated_at, u2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        u1 = User()
        string = f"[{type(u1).__name__}] ({u1.id}) {u1.__dict__}"
        self.assertEqual(u1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        u1 = User()
        old_update = u1.updated_at
        u1.save()
        self.assertNotEqual(u1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        u1 = User()
        u2 = User(**u1.to_dict())
        a_dict = u2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(u2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(u1, u2)


if __name__ == "__main__":
    unittest.main()
