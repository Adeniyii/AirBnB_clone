#!/usr/bin/python3
"""The `city` module

It defines one class, `City(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A city in the application.

    Attributes:
        name
        state_id
    """
    name = ""
    state_id = ""
