#!/usr/bin/python3
"""Unit tests for the `state` module.
"""
import unittest
from models.user import User
from models import storage
from datetime import datetime

u1 = User()
u2 = User(**u1.to_dict())
u3 = User("hello", "wait", "in")

class TestState(unittest.TestCase):
	"""Test cases for the `User` class."""

	def test_params(self):
		k = f"{type(a1).__name__}.{a1.id}"
		self.assertIsInstance(u1.email, "")
		self.assertIsInstance(u1.password, str)
		self.assertIsInstance(u1.first_name, str)
		self.assertIsInstance(u1.last_name, str)

if __name__ == "__main__":
	unittest.main()