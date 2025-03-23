#!/usr/bin/python3
"""This module defines the entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone"""
    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_create(self, args):
        """Creates a new instance of a class"""
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[args]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Shows the string representation of an instance"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
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
        if args[0] not in self.classes:
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
        elif args in self.classes:
            print([str(obj) for key, obj in objs.items() if key.startswith(args)])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
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

    def do_count(self, args):
        """Counts the number of instances of a class"""
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for key in storage.all() if key.startswith(args + "."))
        print(count)

    def default(self, line):
        """Handles commands in the format <class name>.command(<id>)"""
        if "." in line:
            class_name, command = line.split(".", 1)
            if "(" in command and ")" in command:
                command_name, args = command.split("(", 1)
                args = args[:-1]  # Remove the closing parenthesis
                args = args.replace('"', '').replace("'", "")  # Remove quotes from arguments
                if command_name == "show":
                    self.do_show(f"{class_name} {args}")
                elif command_name == "all":
                    self.do_all(class_name)
                elif command_name == "count":
                    self.do_count(class_name)
                else:
                    print("** command not found **")
            else:
                print("** command not found **")
        else:
            print("** command not found **")

    def do_quit(self, args):
        """Exits the console"""
        return True

    def do_EOF(self, args):
        """Exits the console"""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()