import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime

b1 = BaseModel()
b2 = BaseModel(**b1.to_dict())
b3 = BaseModel("hello", "wait", "in")


class TestBase(unittest.TestCase):
    """Test cases for the `Base` class."""

    def test_params(self):
        """Test method for class attributes"""

        k = f"{type(b1).__name__}.{b1.id}"

        self.assertIn(k, storage.all())
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertEqual(b1.created_at, b2.created_at)
        self.assertEqual(b1.id, b2.id)

    def test_dict(self):
        """Test method for dict"""

        b1_dict = b1.to_dict()
        self.assertIsInstance(b1.to_dict(), dict)
        self.assertEqual(b1_dict['__class__'], type(b1).__name__)
        self.assertIn('created_at', b1_dict.keys())
        self.assertIn('updated_at', b1_dict.keys())
        self.assertNotEqual(b1, b2)

    def test_save(self):
        """Test method for save"""

        old_update = b1.updated_at
        b1.save()
        self.assertNotEqual(b1.updated_at, old_update)

    def test_str(self):
        """Test method for str representation"""

        string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        self.assertEqual(b1.__str__(), string)


if __name__ == "__main__":
    unittest.main()
