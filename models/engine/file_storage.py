#!/usr/bin/python3
"""
Module: file_storage.py
"""
import os
import json
from models.base_model import BaseModel


class FileStorage():
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        # change occurrences of self.* to obj.*
        key = "{}.{}".format(type(obj).__name__, obj.id)
        # the `obj` should be saved in __objects,
        # not the __dict__ of the Filestorage instance.
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        # change all uses of self.__file_path and self.__objects
        # to FileStorage.__file_path and FileStorage.__objects
        with open(FileStorage.__file_path, 'w') as f:
            # the objects should be converted to dicts before
            # calling json.dump()
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, does nothing
        """
        # if file doesn't exist, do nothing
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized = json.load(f)
            # if nothing was loaded, do nothing => __object will remain as {}
            if deserialized is None:
                return

            # the deserialized objects should be converted to an instance
            # and set in FileStorage.__objects, not returned.
            FileStorage.__objects = {
                k: BaseModel(**v) for k, v in deserialized.items()}
