#!/usr/bin/python3 
"""Describes the city class,derived from the basemodel class"""
from models.base_model import BaseModel

class City(BaseModel):
    """This class represents a city

    Class attributes
    state_id(str):The id of the city
    name(str): The name of the city

    """

    state_id = ""
    name = ""
