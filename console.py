#!/usr/bin/python3
"""this file is containing a program called console.py
that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """define a new class HBNBCCommand """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF to exit the program"""
        print()
        return True

    def emptyline(self):
        """to make sure that an empty line + ENTER should not execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
