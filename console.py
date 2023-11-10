#!/usr/bin/python3
"""this file is containing a program called console.py
that contains the entry point of the command interpreter"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """define a new class HBNBCCommand """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF to exit the program"""
        print()
        return True

    def emptyline(self):
        """to make sure that an empty line
        + ENTER should not execute anything"""
        pass




    def do_create(self, line):
        """to creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        Ex: $ create BaseModel"""


    def do_show(self,line):    
        """to prints the string representation of an
        instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234"""


    def do_destroy(self, line):
        """to deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234"""



    def do_all(self, line):
        """to prints all string representation of all
        instances based or not on the class name.
        Ex: $ all BaseModel or $ all"""

    def do_update(self, line):
        """to updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
