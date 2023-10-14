#!/usr/bin/python3
"""This module defines a FileStorage Class"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

CLASSES = {"BaseModel": BaseModel,
           "User": User,
           "State": State,
           "City": City,
           "Amenity": Amenity,
           "Place": Place,
           "Review": Review}


class FileStorage():
    """This is the FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Adds obj to __objects with obj.id as key"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file path __file_path"""
        with open(self.__file_path, 'w') as outfile:
            serialized = {key: value.to_dict()
                          for key, value in self.__objects.items()}
            outfile.write(json.dumps(serialized))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as infile:
                deserialized = json.loads(infile.readline())
            for key, value in deserialized.items():
                class_name = key.split('.')[0]
                Constructor = CLASSES.get(class_name, None)
                if Constructor:
                    self.__objects[key] = Constructor(**value)
        except Exception as ex:
            pass
