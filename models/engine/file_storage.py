#!/usr/bin/python3
from json import dump, load



"""config_open = { "errors": "ignore", encoding: "utf-8"}"""

"""file_storage.py"""
class FileStorage:
    __file_path = str("file.json")
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
       key = "{}.{}".format(type(obj).__name__, obj.id)
       self.__objects[key] = obj

    def save(self):
        json_serialized = dict()
        for key, value in self.__objects.items():
            json_serialized[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as current_file:
            dump(json_serialized, current_file)

    def reload(self):
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        try:
            with open(self.__file_path, 'r') as current_file:
                json_deserialized = load(current_file)
                for key, value in json_deserialized.items():
                    instance_format = "{}(**value)".format(value["__class__"])
                    self.__objects[key] = eval(instance_format)
        except (FileNotFoundError):
            pass

