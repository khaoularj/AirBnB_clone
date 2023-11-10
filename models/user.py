#!/usr/bin/python3
"""define a new class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """this class inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
