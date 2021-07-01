#!/usr/bin/python3
""" command line insterprete of a AirBnB """
import cmd
from models.base_model import BaseModel
from models import storage
import models

def valid_line(line):
        if not line:
            print("** class name missing **")
            return False
        else:
            return True

class HBNBCommand(cmd.Cmd):
    """
    command line interpreter handler to loop and interact within classes.\n
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """ handles the event when entering an empty line. """
        pass

    def do_create(self, line):
        """ handles the event when entering an empty line. """
        if not valid_line(line):
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
        """ handles the event when entering an empty line. """
        if not valid_line(line):
            return
        try:
            dic_objects = models.storage.all()
            words = line.split()
            if len(words) < 2:
                print("** instance id missing **")
                return;
            class_to_intance = eval(words[0])
            if issubclass(class_to_intance, BaseModel):
                key = "{}.{}".format(words[0], words[1])
                print(key)
                if key in dic_objects.keys():
                    print(dic_objects[key])
                else:
                    print("** no instance found **")
            else:
                raise NameError
        except (NameError):
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """ handles the event when entering an empty line. """
        if not valid_line(line):
            return
        try:
            dic_objects = models.storage.all()
            words = line.split()
            if len(words) < 2:
                print("** instance id missing **")
                return;
            class_to_intance = eval(words[0])
            if issubclass(class_to_intance, BaseModel):
                key = "{}.{}".format(words[0], words[1])
                if key in dic_objects.keys():
                    del dic_objects[key]
                else:
                    print("** no instance found **")
            else:
                raise NameError
        except (NameError):
            print("** class doesn't exist **")

    def do_all(self, line):
        """ handles the event when entering an empty line. """
        storage.reload()
        dic_objects = models.storage.all()
        list_of_strings = []

        if line == "":
            for obj_id, obj in dic_objects.items():
                list_of_strings.append(obj.__str__())
            if bool(list_of_strings):
                print(list_of_strings)
        else:
            words = line.split()
            if len(words) == 1 and words[0].isalpha():
                try:
                    class_to_intance = eval(words[0])
                    if issubclass(class_to_intance, BaseModel):
                        for obj_id, obj in dic_objects.items():
                            class_name = obj_id.split(".")
                            if words[0] == class_name[0]:
                                list_of_strings.append(obj.__str__())
                        if bool(list_of_strings):
                            print(list_of_strings)
                    else:
                        raise NameError
                except (NameError):
                    print("** class doesn't exist **")

    def do_update(self, line):
        """ handles the event when entering an empty line. """
        arg_sp = line.split()
        dic_objects = models.storage.all()

        if len(arg_sp) == 0:
            print("** class name missing **")

        try:
            class_to_intance = eval(arg_sp[0])
            if not issubclass(class_to_intance, BaseModel):
                print("** class doesn't exist **")
            elif len(arg_sp) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(arg_sp[0], arg_sp[1]) not in dic_objects.keys():
                print("** no instance found **")
            elif len(arg_sp) == 2:
                print("** attribute name missing **")
            elif len(arg_sp) == 3:
                print("** value missing **")
            else:
                format_key = "{}.{}".format(arg_sp[0], arg_sp[1])
                try:
                    setattr(dic_objects[format_key], arg_sp[2], eval(arg_sp[3]))
                except NameError:
                    setattr(dic_objects[format_key], arg_sp[2], arg_sp[3])
            models.storage.save()
        except (NameError):
            print("** class doesn't exist **")

    def do_count(self, arg):
        """ handles the event when entering an empty line. """
        dic_objects = models.storage.all()
        arg_sp = arg.split()
        counter = 0
        for objs in dic_objects.values():
            if arg_sp[0] == type(objs).__name__:
                counter += 1
        print(counter)

    def default(self, line):
        """ handles the event when entering an empty line. """

        functions = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }

        line = (line.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            cmd_arg = line[0] + " " + line[2]
            func = functions[line[1]]
            func(cmd_arg)
        except:
            print("*** Unknown syntax:", line[0])

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
