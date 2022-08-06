#!/usr/bin/python3
"""Defines unittests for console.py.
"""
from io import StringIO
import unittest
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """"""

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_simple(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
