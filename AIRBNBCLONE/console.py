#!/usr/bin/python3
"""This module defines the entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone"""
    prompt = "(hbnb) "

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    # Add other commands like `show`, `destroy`, `all`, `update`


if __name__ == "__main__":
    HBNBCommand().cmdloop()