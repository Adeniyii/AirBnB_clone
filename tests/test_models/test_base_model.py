import unittest
from models.base_model import BaseModel
from datetime import datetime

b1 = BaseModel()
b2 = BaseModel(**b1.to_dict())

class TestBase(unittest.TestCase):

	def test_basic(self):
		b1.name = "Cecilia"
		b1.email = "catabong89@gmail.com"

		self.assertIsInstance(b1.id, str)
		self.assertIsInstance(b1.created_at, datetime)
		self.assertIsInstance(b1.created_at, datetime)
		self.assertEqual(b1.name, "Cecilia")
		self.assertEqual(b1.email, "catabong89@gmail.com")
		self.assertEqual(b1.created_at, b2.created_at)
		self.assertEqual(b1.id, b2.id)

	def test_dict(self):
		b1_dict = b1.to_dict()
		self.assertIsInstance(b1.to_dict(), dict)

	def test_save(self):
		b1.save()
		self.assertGreater(b1.updated_at, b1.created_at)

if __name__ == "__main__":
	unittest.main()