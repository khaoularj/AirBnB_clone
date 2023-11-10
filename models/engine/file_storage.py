#!/usr/bin/python3
"""Define a new class called FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """this is the FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instance"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """adding public instance methods
        that returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """adding public instance methods that  sets in
        __objects the obj with key <obj class name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """adding public instance methods that serializes
        __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            data_file = {
                    key: value.to_dict()
                    for key, value in FileStorage.__objects.items()
                    }
            json.dump(data_file, f)

    def reload(self):
        """adding public instance methods that deserializes
        the JSON file to __objects (only if the JSON file (__file_path) exists
        if not, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                data_file = json.load(f)
                for k, v in data_file.items():
                    class_name, obj_id = k.split(".")
                    obj = globals()[class_name](**v)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
