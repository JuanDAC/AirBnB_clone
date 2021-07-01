#!/usr/bin/python3
"""Defines a Review class that inherits from BaseModel"""

from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """Represents the Review class inherit from BaseModel

        Args:
            place_id (str): The name id of the place.
            user_id (str): The user id of the user.
    """
    place_id = ""
    user_id = ""
    text = ""
