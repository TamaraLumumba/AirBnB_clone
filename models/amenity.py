#!/usr/bin/python3
"""Defines the Amenity class, which is derived from the BaseModel class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class represents an Amenity

    Class Attributes:
    name(str): The name of the amenity
    """
    name = ""
