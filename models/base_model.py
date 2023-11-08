#!/usr/bin/python3
"""Define class called BaseModel"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """this is the BaseModel that defines all
    common attributes/methods for other classes"""

    """def __init__(self):
        this is a new class constructor that initialize a new BaseModel
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()"""
    def __init__(self, *args, **kwargs):
        """this is a new class constructor that initialize a new BaseModel
        Args:
            *args: unused argument
            **Kwargs: Key/value pairs of attributes"""
        if kwargs:
            kwargs.pop("__class__", None)
            self.__dict__.update(kwargs)
            self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """adding the public methods that updates the public
        instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """adding the public method that returns
        a dictionary containing all keys/values of __dict__ of the instance"""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def __str__(self):
        """overriding the __str__ method so that
        it print: [<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
