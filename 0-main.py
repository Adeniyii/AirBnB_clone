#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City

a1 = City()
print(a1.name)
a1.name = 'Abuja'
print(a1.name)

