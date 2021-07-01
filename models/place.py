#!/usr/bin/python3
"""Defines a Review class that inherits from BaseModel"""

from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity


class Place(BaseModel):
    """Represents the Place class inherit from BaseModel

        Args:
            city_id (str): The city id of the place.
            user_id (str): The user id of the place.
            name (str): The name of the place.
            description (str): The description of the place.
            number_rooms (int): The number rooms of the place.
            number_bathrooms (int): The number bathrooms of the place.
            max_guest (int): The max guest of the place.
            price_by_night (int): The price by night.
            latitude (float): The loatitude coordinate.
            longitude (float): The longitude coordinate.
            amenity_ids (list): Will be the User.id
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
