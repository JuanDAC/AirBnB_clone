#!/usr/bin/python3
"""Defines a State class that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents the State class inherit from BaseModel with there arguments:

        Args:
        name (Str): The name of the state.
    """
    name = ""
