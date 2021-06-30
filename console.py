#!/usr/bin/python3
""" command line insterprete of a AirBnB """
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    command line interpreter handler to loop and interact within classes.\n
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """ handles the event when entering an empty line. """
        pass

    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return
        try:
            class_to_intance = eval(line)
            if issubclass(class_to_intance, BaseModel):
                instance = class_to_intance()
                storage.new(instance)
                storage.save()
                print(instance.id)
            else:
                raise NameError
        except (NameError):
            print("** class doesn't exist **")

    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return
        try:
            class_to_intance = eval(line)
            if issubclass(class_to_intance, BaseModel):
                instance = class_to_intance()
                storage.new(instance)
                storage.save()
                print(instance.id)
            else:
                raise NameError
        except (NameError):
            print("** class doesn't exist **")

    def do_quit(self, line):
        """ \033[32m ├»\033[92m Exits the HBNBCommand.\n \033[0m"""
        print("")
        return True

    def do_EOF(self, line):
        """ \033[32m ├»\033[92m Exits the HBNBCommand.\n \033[0m"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
