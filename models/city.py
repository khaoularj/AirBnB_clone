#!/usr/bin/python3
"""define a new class called City"""
from models.base_model import BaseModel


class City(BaseModel):
    """this class inherits from BaseModel"""
    state_id = ""
    name = ""
