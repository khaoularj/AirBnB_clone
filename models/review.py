#!/usr/bin/python3
"""define a new class called Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """this class inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
