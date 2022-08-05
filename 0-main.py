#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity

a1 = Amenity()
print(a1.name)
a1.name = 'hello'
print(a1.name)

