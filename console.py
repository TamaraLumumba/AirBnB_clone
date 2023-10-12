#!/usr/bin/python3
import cmd

class HBNBCommand (cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on receiving an empty line"""
        pass

    def do_quit(self, arg):
        """Command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """"Command to quit th program\n"""
        return True

    def do_create(self, arg):
        """Command that creates a new instance of the BaseModel"""

        if not self.check_class(args):
            return

        instance = HBNBCommand.classes[args]()
        instance.save()
        print(instance.id)

if __name__ == '__main__':
HBNBCommand().cmdloop()
