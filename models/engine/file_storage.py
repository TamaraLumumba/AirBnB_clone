#!/usr/bin/python3
"""Defines class FileStorage."""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.place import Place


class FileStorage:
    """The storage engine.

    Attributes:
        __file_path (str): Name of the file to save objects to.
        __objects (dict): A dictionary of the objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        keyname = obj.__class__.__name__
        self.__objects["{}.{}".format(keyname, obj.id)] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        dict1 = self.__objects
        objdict = {obj: dict1[obj].to_dict() for obj in dict1.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file objects."""
        try:
            with open(self.__file_path) as f:
                objdict = json.load(f)
                for value in objdict.values():
                    clsname = value["__class__"]
                    del value["__class__"]
                    self.new(eval(clsname)(**value))
        except FileNotFoundError:
            return
