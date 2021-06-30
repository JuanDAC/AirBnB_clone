#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def emptyline(self):
        """ Handles the event when entering an empty line. """
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
