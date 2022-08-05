#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity

a1 = Amenity('name', 'wait')
string = f"[{type(a1).__name__}] ({a1.id}) {a1.__dict__}"
print(a1.name)


