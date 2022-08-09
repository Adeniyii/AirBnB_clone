#!/usr/bin/python3
"""Defines unittests for console.py.
"""
from io import StringIO
import unittest
from unittest.mock import patch
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


class TestConsole(unittest.TestCase):
    """Base class for testing Console"""

    def setUp(self) -> None:
        """No idea"""
        return super().setUp()

    def tearDown(self) -> None:
        """No idea"""
        return super().tearDown()

    def test_simple(self):
        """Tests basic commands"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIsInstance(f.getvalue(), str)

    def test_create(self):
        """Tests the create command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertIn(f"BaseModel.{f.getvalue().strip()}",
                          storage.all().keys())

    def test_show(self):
        """Tests the show command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.show({b1.id})'))
            res = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

        with patch('sys.stdout', new=StringIO()) as f:
            u1 = User()
            HBNBCommand().onecmd(HBNBCommand().precmd(f'User.show({u1.id})'))
            res = f"[{type(u1).__name__}] ({u1.id}) {u1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

        with patch('sys.stdout', new=StringIO()) as f:
            s1 = State()
            HBNBCommand().onecmd(HBNBCommand().precmd(f'State.show({s1.id})'))
            res = f"[{type(s1).__name__}] ({s1.id}) {s1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

        with patch('sys.stdout', new=StringIO()) as f:
            c1 = City()
            HBNBCommand().onecmd(HBNBCommand().precmd(f'City.show({c1.id})'))
            res = f"[{type(c1).__name__}] ({c1.id}) {c1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

        with patch('sys.stdout', new=StringIO()) as f:
            a1 = Amenity()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.show({a1.id})'))
            res = f"[{type(a1).__name__}] ({a1.id}) {a1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

        with patch('sys.stdout', new=StringIO()) as f:
            p1 = Place()
            HBNBCommand().onecmd(HBNBCommand().precmd(f'Place.show({p1.id})'))
            res = f"[{type(p1).__name__}] ({p1.id}) {p1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

        with patch('sys.stdout', new=StringIO()) as f:
            r1 = Review()
            HBNBCommand().onecmd(HBNBCommand().precmd(f'Review.show({r1.id})'))
            res = f"[{type(r1).__name__}] ({r1.id}) {r1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update(self):
        """Tests the update command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.update({b1.id}, "name", "Ife")'))
            self.assertEqual(b1.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            u1 = User()
            u1.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update({u1.id}, "name", "Ifedayo")'))
            self.assertEqual(u1.__dict__["name"], "Ifedayo")

        with patch('sys.stdout', new=StringIO()) as f:
            s1 = State()
            s1.name = "Lagos"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update({s1.id}, "name", "Abuja")'))
            self.assertEqual(s1.__dict__["name"], "Abuja")

        with patch('sys.stdout', new=StringIO()) as f:
            p1 = Place()
            p1.name = "Ikoyi"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.update({p1.id}, "name", "Ikeja")'))
            self.assertEqual(p1.__dict__["name"], "Ikeja")

        with patch('sys.stdout', new=StringIO()) as f:
            c1 = City()
            c1.name = "Iba"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.update({c1.id}, "name", "Badagry")'))
            self.assertEqual(c1.__dict__["name"], "Badagry")

        with patch('sys.stdout', new=StringIO()) as f:
            a1 = Amenity()
            a1.name = "Room service"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.update({a1.id}, "name", "Hottub")'))
            self.assertEqual(a1.__dict__["name"], "Hottub")

        with patch('sys.stdout', new=StringIO()) as f:
            r1 = Review()
            r1.name = "Ominious"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update({r1.id}, "name", "Sin")'))
            self.assertEqual(r1.__dict__["name"], "Sin")

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.update({b1.id}, {{"name":"I"}})'))
            self.assertEqual(b1.__dict__["name"], "I")

        with patch('sys.stdout', new=StringIO()) as f:
            u1 = User()
            u1.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update({u1.id}, {{"name": "Ife"}})'))
            self.assertEqual(u1.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            s1 = State()
            s1.name = "Lagos"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update({s1.id}, {{"name": "Abu"}})'))
            self.assertEqual(s1.__dict__["name"], "Abu")

        with patch('sys.stdout', new=StringIO()) as f:
            p1 = Place()
            p1.name = "Ikoyi"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.update({p1.id}, {{"name": "Ike"}})'))
            self.assertEqual(p1.__dict__["name"], "Ike")

        with patch('sys.stdout', new=StringIO()) as f:
            c1 = City()
            c1.name = "Iba"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.update({c1.id}, {{"name": "Bada"}})'))
            self.assertEqual(c1.__dict__["name"], "Bada")

        with patch('sys.stdout', new=StringIO()) as f:
            a1 = Amenity()
            a1.name = "Room service"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.update({a1.id}, {{"name":"Hot"}})'))
            self.assertEqual(a1.__dict__["name"], "Hot")

        with patch('sys.stdout', new=StringIO()) as f:
            r1 = Review()
            r1.name = "Ominious"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update({r1.id}, {{"name": "Sin"}})'))
            self.assertEqual(r1.__dict__["name"], "Sin")

    def test_all(self):
        """Tests the all command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('City.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[City]')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Amenity.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Amenity]')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Place.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Place]')

    def test_count(self):
        """Tests the count command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == BaseModel:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == User:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('City.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == City:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Place.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Place:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == State:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Amenity.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Amenity:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Review:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_destroy(self):
        """Tests the destroy command"""

        with patch('sys.stdout', new=StringIO()) as f:
            io = BaseModel()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.destroy({io.id})'))
            for key in storage.all().keys():
                self.assertNotIn(key, io.id)

        with patch('sys.stdout', new=StringIO()) as f:
            io = User()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.destroy({io.id})'))
            for key in storage.all().keys():
                self.assertNotIn(key, io.id)

        with patch('sys.stdout', new=StringIO()) as f:
            io = State()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.destroy({io.id})'))
            for key in storage.all().keys():
                self.assertNotIn(key, io.id)

        with patch('sys.stdout', new=StringIO()) as f:
            io = City()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.destroy({io.id})'))
            for key in storage.all().keys():
                self.assertNotIn(key, io.id)

        with patch('sys.stdout', new=StringIO()) as f:
            io = Place()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.destroy({io.id})'))
            for key in storage.all().keys():
                self.assertNotIn(key, io.id)

        with patch('sys.stdout', new=StringIO()) as f:
            io = Review()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.destroy({io.id})'))
            for key in storage.all().keys():
                self.assertNotIn(key, io.id)

        with patch('sys.stdout', new=StringIO()) as f:
            io = Amenity()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.destroy({io.id})'))
            for key in storage.all().keys():
                self.assertNotIn(key, io.id)
