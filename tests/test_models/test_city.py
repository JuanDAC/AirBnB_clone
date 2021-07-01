#!/usr/bin/python3
"""Unittest for state
"""


import unittest
from models.base_model import BaseModel
from models.city import City
import os
import uuid
import datetime
from models.engine.file_storage import FileStorage
from models import storage


class Test_City_class(unittest.TestCase):
    """
    Defines a class to evaluate diferent test cases for city
    """
    def setUp(self):
        """set environment to start testing"""
        # Empty objects in engine
        FileStorage._FileStorage__objects = {}
        # Remove file.json if exists
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """set enviroment when testing is finished"""
        # Empty objects in engine
        FileStorage._FileStorage__objects = {}
        # Remove file.json if exists
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_type_id_class(self):
        """
        Checks for a instance of the class
        """
        my_city = City()
        self.assertIsInstance(my_city, City)
        self.assertIsInstance(my_city, BaseModel)
        self.assertFalse(type(my_city) == type(City))
        self.assertFalse(id(my_city) == id(City))
        my_city_2 = City()
        self.assertTrue(type(my_city) == type(my_city_2))
        self.assertFalse(id(my_city) == id(my_city_2))

    def test_instances_attributes(self):
        """
        Checks attributes created to the new object
        """
        # Checks that base attributes are created for the object
        my_city = City()
        my_attrs = ['id', 'created_at', 'updated_at']
        for attr in my_attrs:
            self.assertEqual(attr in my_city.__dict__.keys(), True)

        # Checks for class attributes
        self.assertTrue(hasattr(my_city, 'name'))
        self.assertTrue(hasattr(my_city, 'state_id'))
        # Cheks if class attribute are empty strings
        self.assertEqual(getattr(my_city, 'name'), "")
        self.assertEqual(getattr(my_city, 'state_id'), "")

        # Checks that some falses attributes
        my_attrs = ['name', 'create_time', 'update_time']
        for attr in my_attrs:
            self.assertEqual(attr in my_city.__dict__.keys(), False)

    def test_unique_id(self):
        """
        Checks for a unique id
        """
        # Checks if two instances has diferents id
        my_city = City()
        my_city_2 = City()
        self.assertNotEqual(my_city.id, my_city_2.id)

    def test_datetime(self):
        """
        Checks for datetime attributes
        """
        #Test if two instnace has diferent datetime
        my_city = City()
        my_city_2 = City()
        self.assertNotEqual(my_city.created_at, my_city_2.created_at)
        self.assertNotEqual(my_city.updated_at, my_city_2.updated_at)

        # Test if attribute created_at and updated_at are datetime instance
        my_city = City()
        self.assertIsInstance(my_city.created_at, datetime.datetime)
        self.assertIsInstance(my_city.updated_at, datetime.datetime)

    def test_UUID4(self):
        """
        Checks for the ID generation protocol
        """
        # Checks that the ID generated is the version 4
        my_city = City()
        version = uuid.UUID(my_city.id).version
        self.assertEqual(version, 4)

    def test_created_and_updated_at(self):
        """
        Checks if updated_t attribute changes when a new attribute is
        added to the object and created_at is the same all the time.
        """
        # Checks that updated_at changes
        my_city = City()
        updated_1 = str(my_city.updated_at)
        my_city.name = "New York"
        my_city.save()
        updated_2 = str(my_city.updated_at)
        self.assertNotEqual(updated_1, updated_2)

        # Checks that created_at doesn't change
        my_city = City()
        created_1 = str(my_city.created_at)
        my_city.name = "Chicago"
        my_city.save()
        created_2 = str(my_city.created_at)
        self.assertEqual(created_1, created_2)

    def test_add_new_attributes(self):
        """
        Checks that can add new attributes to the objects
        """
        # Checks new attributes are added
        dict_attr = {'name': 'Betty', 'last': 'Holberton', 'age': 40}
        my_city = City()
        for key, value in dict_attr.items():
            setattr(my_city, key, value)
        for key, value in dict_attr.items():
            self.assertTrue(hasattr(my_city, key))
            self.assertEqual(getattr(my_city, key), value)

        # Checks for all attributes for the object
        my_attrs = ['id', 'created_at', 'updated_at', 'name', 'last', 'age']
        for attr in my_attrs:
            self.assertEqual(attr in my_city.__dict__.keys(), True)

    def test_str_method(self):
        """
        Checks str method
        """
        my_city = City()
        string = "[{}] ({}) {}".format(my_city.__class__.__name__, my_city.id,
                                       my_city.__dict__)
        self.assertEqual(str(my_city), string)

    def test_to_dict_method(self):
        """
        Checks dict method
        """
        # Checks if it convert to a dict type
        my_city = City()
        my_city.name = "Holberton"
        my_city.my_number = 89
        my_city.my_float = 100.54
        my_city.my_list = ["Hello", "world", 100]
        my_city.my_dict = {'name': 'Betty', 'last_name': 'Holberton', 'age': 85}
        my_city.save()
        my_city_json = my_city.to_dict()
        # checks if the method really convert to a dict type all the attributes
        self.assertEqual(type(my_city_json), dict)
        for key, value in my_city_json.items():
            # checks if the dict has the same attributes keys that the object
            self.assertTrue(hasattr(my_city, key))
            # checks if datetime was safe as a iso format and its type
            if key == "created_at" or key == "updated_at":
                _datetime = getattr(my_city, key).isoformat()
                self.assertEqual(_datetime, value)
                self.assertTrue(type(value) == str)
            # checks the class name attribute and its type
            elif key == "__class__":
                self.assertEqual(my_city.__class__.__name__, value)
                self.assertTrue(type(value) == str)
            else:
                #checks the value for others attributes
                self.assertEqual(getattr(my_city, key), value)
                # Checks the types and formats of the attributes
                if key == "id":
                    version = uuid.UUID(value).version
                    self.assertEqual(version, 4)
                    self.assertTrue(type(value), str)
                elif key == "name":
                    self.assertTrue(type(value) == str)
                elif key == "my_number":
                    self.assertTrue(type(value) == int)
                elif key == "my_list":
                    self.assertTrue(type(value) == list)
                elif key == "my_float":
                    self.assertTrue(type(value) == float)
                elif key == "my_dict":
                    self.assertTrue(type(value) == dict)

    def test_init_state_from_dictionary(self):
        """
        Checks when it is passed a dictionary to the init method.
        """
        my_city = City()
        my_city.name = "Holberton"
        my_city.my_number = 89
        my_city_json = my_city.to_dict()
        my_new_my_city = City(**my_city_json)
        # Checks that the object has the same attributes that the my_city
        dict_attr = {'name': 'Holberton', 'my_number': 89, 'id': my_city.id,
                     'created_at': my_city.created_at,
                     'updated_at': my_city.updated_at}
        for key, value in dict_attr.items():
            self.assertTrue(hasattr(my_new_my_city, key))
            self.assertEqual(getattr(my_new_my_city, key), value)
        # Checks if __class__ attribute was not added
        self.assertTrue(hasattr(my_new_my_city, key))
        cls_name = getattr(my_new_my_city, key)
        self.assertNotEqual(cls_name, my_city_json["__class__"])
