#!/usr/bin/python3
"""Unit tests for the `city` module.
"""
import unittest
from models.place import Place

p1 = Place()

class TestPlace(unittest.TestCase):
    """Test cases for the `Place` class."""

    def test_params(self):
        """Test method for class attributes"""
        
        self.assertEqual(p1.name, "")
        self.assertEqual(p1.user_id, "")
        self.assertEqual(p1.city_id, "")
        self.assertEqual(p1.description, "")
        self.assertEqual(p1.number_bathrooms, 0)
        self.assertEqual(p1.number_rooms, 0)
        self.assertEqual(p1.price_by_night, 0)
        self.assertEqual(p1.max_guest, 0)
        self.assertEqual(p1.longitude, 0.0)
        self.assertEqual(p1.latitude, 0.0)
        self.assertEqual(p1.amenity_ids, [])

if __name__ == "__main__":
	unittest.main()
