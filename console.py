#!/usr/bin/python3
""" command line insterprete of a AirBnB """
import cmd


class HBNBCommand(cmd.Cmd):
    """
    command line interpreter handler to loop and interact within classes.\n
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """ handles the event when entering an empty line. """
        pass

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
