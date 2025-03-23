#!/usr/bin/python3
"""This module defines a class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines attributes for a review"""
    place_id = ""
    user_id = ""
    text = ""