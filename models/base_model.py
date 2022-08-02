#!/usr/bin/python3
"""
Module: base.py
"""
import uuid
import re
from datetime import datetime
from models import storage

class BaseModel():
    """
    Base class which defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        instatiates an object with it's
        attributes
        """
        re.compile('/d{2,4}-/d{2,4}-(/d{2}-)*
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key.endswith('ted_at'):
                        value = datetime.fromisoformat(value)
                    setattr(self,key,value)
            return
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns the string representation
        of the instance
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        to_dict = self.__dict__
        to_dict['__class__'] = type(self).__name__
        to_dict['created_at'] = to_dict['created_at'].isoformat()
        to_dict['updated_at'] = to_dict['updated_at'].isoformat()

        return to_dict
