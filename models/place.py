#!/usr/bin/python3
"""Defines class Place."""
from models.base_model import BaseModel


class Place(BaseModel):
    """A place instance.

    Attributes:
        city_id (str): City's id.
        user_id (str): User's id.
        name (str): name of the  place.
        description (str): place description.
        number_rooms (int): Number of rooms available at the place.
        number_bathrooms (int): Number of bathrooms available.
        max_guest (int): Maximum number of guests.
        price_by_night (int): The price per night.
        latitude (float): The of latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list representation of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
