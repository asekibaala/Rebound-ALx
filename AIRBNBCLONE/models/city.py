#!/usr/bin/python3
"""This module defines a class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines attributes for a city"""
    state_id = ""
    name = ""