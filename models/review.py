#!/usr/bin/python3
"""Class Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """A review instance.

    Attributes:
        place_id (str): Id of the place.
        user_id (str): user's Id.
        text (str): text describing customer experience.
    """

    place_id = ""
    user_id = ""
    text = ""
