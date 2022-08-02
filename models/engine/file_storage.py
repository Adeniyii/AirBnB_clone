#!/usr/bin/python3
"""
Module: file_storage.py
"""
import os

class FileStorage():
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    def __init__(self):
        __file_path = "file.json"
        __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage__objects

    def new(self):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(self).__name__, self.id)
        FileStorage__objects[key] = __objects

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        json.loads(__objects)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON 
        file exists ; otherwise, does nothing
        """
        if os.path.exists(__file_path):
            return json.dumps(__file_path)

