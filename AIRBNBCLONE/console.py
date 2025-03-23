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
        """Creates a new instance of a class"""
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Shows the string representation of an instance"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representations of instances"""
        objs = storage.all()
        if not args:
            print([str(obj) for obj in objs.values()])
        elif args in globals():
            print([str(obj) for key, obj in objs.items() if key.startswith(args)])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(obj, args[2], eval(args[3]))
        obj.save()
    def do_quit(self, args):
        """Exits the console"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()        