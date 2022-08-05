#!/usr/bin/python3
"""Unit tests for the `state` module.
"""
import unittest
from models.user import User

u1 = User()

class TestState(unittest.TestCase):
	"""Test cases for the `User` class."""

	def test_params(self):
		self.assertEqual(u1.email, "")
		self.assertEqual(u1.password, "")
		self.assertEqual(u1.first_name, "")
		self.assertEqual(u1.last_name, "")

if __name__ == "__main__":
	unittest.main()