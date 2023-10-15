#!/usr/bin/python3
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.place import Place


class HBNBCommand (cmd.Cmd):
    """Defines command interpreter"""

    prompt = "(hbnb) "

    def my_errors(self, line, num_of_args):
        """Displays error messages to user

        Args:
            line(any): gets user input using command line
            num_of_args(int): number of input arguments
        """
        classes = {"BaseModel",
                   "User",
                   "State",
                   "City",
                   "Place",
                   "Amenity",
                   "Review"}

        msg = ["** class name missing **",
               "** class doesn't exist **",
               "** instance id missing **",
               "** no instance found **",
               "** attribute name missing **",
               "** value missing **"]
        if not line:
            print(msg[0])
            return True
        args = line.split()
        if num_of_args >= 1 and args[0] not in classes:
            print(msg[1])
            return True
        elif num_of_args == 1:
            return False
        if num_of_args >= 2 and len(args) < 2:
            print(msg[2])
            return True
        all_objs = storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        if num_of_args >= 2 and key not in all_objs:
            print(msg[3])
            return True
        elif num_of_args == 2:
            return False
        if num_of_args >= 4 and len(args) < 3:
            print(msg[4])
            return True
        if num_of_args >= 4 and len(args) < 4:
            print(msg[5])
            return True
        return False

    def emptyline(self):
        """Do nothing on receiving an empty line"""
        pass

    def do_quit(self, arg):
        """Command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """"Command to quit th program\n"""
        return True

    def do_create(self, line):
        """Command that creates a new instance of the BaseModel"""
        if (self.my_errors(line, 1) is True):
            return
        args = line.split(" ")
        obj = eval(args[0])()
        obj.save()

        print(obj.id)

    def do_show(self, line):
        """Prints a string representation of an instance.

        Args:
            line: line to enter with command
            Example: 'show User 7'

        """
        if (self.my_errors(line, 2) is True):
            return
        args = line.split()
        all_objs = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        print(all_objs[key])

    def do_destroy(self, line):
        """Deletes an instance of a certain class.

        Args:
            line: args to enter with command
            example: 'destroy User 10'

        """
        if (self.my_errors(line, 2) is True):
            return
        args = line.split()
        all_objs = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        del all_objs[key]
        storage.save()

    def do_all(self, line):
        """Shows all instances, or instances of a certain class

        Args:
        line : args to enter with command
        """
        all_objs = storage.all()
        if not line:
            print([str(x) for x in all_objs.values()])
            return
        args = line.split()
        if (self.my_errors(line, 1) is True):
            return
        print([str(v) for v in all_objs.values()
               if v.__class__.__name__ == args[0]])

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating an attribute

        Args:
            line : args that receive the commands
        """
        if (self.my_errors(line, 4) is True):
            return
        args = line.split()
        all_objs = storage.all()
        for i in range(len(args[1:]) + 1):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        my_key = args[2]
        my_value = args[3]
        try:
            if my_value.isdigit():
                my_value = int(my_value)
            elif float(my_value):
                my_value = float(my_value)
        except ValueError:
            pass
        class_attr = type(all_objs[key]).__dict__
        if my_key in class_attr.keys():
            try:
                my_value = type(class_attr[my_key])(my_value)
            except Exception:
                print("Entered wrong value type")
                return
        setattr(all_objs[key], my_key, my_value)
        storage.save()

if __name__ == '__main__':
HBNBCommand().cmdloop()
