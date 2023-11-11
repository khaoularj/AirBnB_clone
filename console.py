#!/usr/bin/python3
"""this file is containing a program called console.py
that contains the entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from shlex import split
import re


def parse_cmd(arg):
    """this function parse the command arguments."""
    brackets_start = arg.find("[")
    brackets_end = arg.find("]")

    curly_start = arg.find("{")
    curly_end = arg.find("}")

    if brackets_start == -1 and curly_start == -1:
        return [i.strip(",") for i in split(arg)]
    elif brackets_start == -1 or (
            curly_start != -1 and curly_start < brackets_start):
        lexer = split(arg[:curly_start])
        retl = [i.strip(",") for i in lexer]
        retl.append(arg[curly_start:curly_end + 1])
        return retl
    else:
        lexer = split(arg[:brackets_start])
        retl = [i.strip(",") for i in lexer]
        retl.append(arg[brackets_start:brackets_end + 1])
        return retl


class HBNBCommand(cmd.Cmd):
    """define a new class HBNBCommand """
    prompt = "(hbnb) "
    classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"}

    def default(self, arg):
        """this function handle the invalid input for unknown commands."""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        parts = arg.split('.', 1)
        if len(parts) == 2:
            command, rest = parts
            match = re.match(r"(\w+)\((.*?)\)$", rest)
            if match:
                func_name, args = match.groups()
                if func_name in arg_dict:
                    call = "{} {}".format(command, args)
                    return arg_dict[func_name](call)
        print("*** Unknown syntax: {}".format(arg))

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

    def do_create(self, arg):
        """to creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        Ex: $ create BaseModel"""
        arg_list = parse_cmd(arg)
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """to prints the string representation of an
        instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234"""
        arg_list = parse_cmd(arg)
        obj_dict = storage.all()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """to deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234"""
        arg_list = parse_cmd(arg)
        obj_dict = storage.all()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg):
        """to prints all string representation of all
        instances based or not on the class name.
        Ex: $ all BaseModel or $ all"""
        arg_list = parse_cmd(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj_list = [str(obj) for obj in storage.all().values()
                        if len(arg_list) == 0 or
                        arg_list[0] == obj.__class__.__name__]
            print(obj_list)

    def do_count(self, arg):
        """to retrieve the number of instances of a class:
            <class name>.count()"""
        arg_list = parse_cmd(arg)
        count = sum(
                1 for obj in storage.all().values()
                if arg_list[0] == obj.__class__.__name__)
        print(count)

    def do_update(self, arg):
        """to updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""
        arg_list = parse_cmd(arg)
        obj_dict = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_list) == 4:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = val_type(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            for k, v in eval(arg_list[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    val_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = val_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
