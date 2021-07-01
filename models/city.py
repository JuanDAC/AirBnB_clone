#!/usr/bin/python3

from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """Represents the City class inherit from BaseModel with there arguments:

        Args:
            state_id (Str): The name of the city.
            name (Str): The name of the city.
    """
    state_id = ""
    name = ""
