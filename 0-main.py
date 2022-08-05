#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity

a1 = Amenity('name', 'wait')
old_update = a1.updated_at
print(old_update)
a1.save()
print(a1.updated_at)

