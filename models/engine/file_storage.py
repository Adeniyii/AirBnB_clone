#!/usr/bin/python3
"""
Module: file_storage.py
"""
import os
import json

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

    def new(self):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(self).__name__, self.id)
        __objects[key] = self.__dict__

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        with open(self.__file_path, 'w') as file:
            json.dump(__objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON 
        file exists; otherwise, does nothing
        """
        if os.path.exists(self.__file_path):
            print(self.__objects)
            with open(self.__file_path, 'r') as f:

                    results = json.load(f)

                    if results is None:
                        return []
                    
                    return "works"
        return []
                

