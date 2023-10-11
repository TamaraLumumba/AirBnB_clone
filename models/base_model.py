#!/usr/bin/python3
"""Defines BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The BaseModel of the AirBnB clone project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args : tuple representation of arguments. Unused.
            **kwargs : Key/value pairs of arguments.
        """
        timef = "%d-%m-%yT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timef)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """save updated_at current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns the dictionary of the BaseModel instance."""

        basedict = self.__dict__.copy()
        basedict["created_at"] = self.created_at.isoformat()
        basedict["updated_at"] = self.updated_at.isoformat()
        basedict["__class__"] = self.__class__.__name__
        return basedict

    def __str__(self):
        """Returns the print/str representation of the BaseModel instance."""
        cname = self.__class__.__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)
