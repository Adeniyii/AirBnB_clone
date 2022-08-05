#!/usr/bin/python3
"""Unit tests for the `review` module.
"""
import unittest
from models.review import Review

r1 = Review()

class TestReview(unittest.TestCase):
    """Test cases for the `Review` class."""

    def test_params(self):
        """Test method for class attributes"""

        self.assertEqual(r1.text, "")
        self.assertEqual(r1.user_id, "")
        self.assertEqual(r1.place_id, "")

if __name__ == "__main__":
	unittest.main()