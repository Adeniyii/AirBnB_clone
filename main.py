#!/usr/bin/python3
"""Defines unittests for console.py.
"""
from io import StringIO
import os
import unittest
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestUserDotNotation(unittest.TestCase):
    """Testing commands using dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """Test create basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'User.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_basemodel(self):
        """Test count basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == User:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_basemodel(self):
        """Test all basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_basemodel(self):
        """Test show basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.show({us.id})'))
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_basemodel(self):
        """Test update basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update({us.id}, name, "Ife")'))
            self.assertEqual(us.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update({us.id}, age, 25)'))
            self.assertIn("age", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 60
            cmmd = f'User.update({us.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", us.__dict__.keys())
            self.assertNotIn("color", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 10)

    def test_update_basemodel_dict(self):
        """Test update basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            cmmd = f'User.update({us.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(us.__dict__["age"], 25)
            self.assertIsInstance(us.__dict__["age"], int)

    def test_destroy_basemodel(self):
        """Test destroy basemodel object.
        """
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.destroy({us.id})'))
            self.assertNotIn("User.{}".format(
                us.id), storage.all().keys())
