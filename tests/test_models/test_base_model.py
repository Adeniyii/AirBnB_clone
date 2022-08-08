"""Testing the `base_model` module."""
import json
import os
import time
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    """Test cases for the `Base` class.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization_positive(self):
        """Test passing cases `BaseModel` initialization.
        """
        b1 = BaseModel()
        b2_uuid = str(uuid.uuid4())
        b2 = BaseModel(id=b2_uuid, name="The weeknd", album="Trilogy")
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b2.id, str)
        self.assertEqual(b2_uuid, b2.id)
        self.assertEqual(b2.album, "Trilogy")
        self.assertEqual(b2.name, "The weeknd")
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertEqual(str(type(b1)),
                         "<class 'models.base_model.BaseModel'>")

    def test_dict(self):
        """Test method for dict"""
        b1 = BaseModel()
        b2_uuid = str(uuid.uuid4())
        b2 = BaseModel(id=b2_uuid, name="The weeknd", album="Trilogy")
        b1_dict = b1.to_dict()
        self.assertIsInstance(b1_dict, dict)
        self.assertIn('id', b1_dict.keys())
        self.assertIn('created_at', b1_dict.keys())
        self.assertIn('updated_at', b1_dict.keys())
        self.assertEqual(b1_dict['__class__'], type(b1).__name__)
        with self.assertRaises(KeyError) as e:
            b2.to_dict()

    def test_save(self):
        """Test method for save"""
        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_save_storage(self):
        """Tests that storage.save() is called from save()."""
        b = BaseModel()
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_str(self):
        """Test method for str representation"""
        b1 = BaseModel()
        string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        self.assertEqual(b1.__str__(), string)


if __name__ == "__main__":
    unittest.main()
