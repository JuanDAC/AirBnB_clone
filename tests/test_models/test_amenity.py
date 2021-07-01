#!/usr/bin/python3
"""Unittest for state
"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import os
import uuid
import datetime
from models.engine.file_storage import FileStorage
from models import storage


class Test_Amenity_class(unittest.TestCase):
    """
    Defines a class to evaluate diferent test cases for amenity
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
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)
        self.assertIsInstance(my_amenity, BaseModel)
        self.assertFalse(type(my_amenity) == type(Amenity))
        self.assertFalse(id(my_amenity) == id(Amenity))
        my_amenity_2 = Amenity()
        self.assertTrue(type(my_amenity) == type(my_amenity_2))
        self.assertFalse(id(my_amenity) == id(my_amenity_2))

    def test_instances_attributes(self):
        """
        Checks attributes created to the new object
        """
        # Checks that base attributes are created for the object
        my_amenity = Amenity()
        my_attrs = ['id', 'created_at', 'updated_at']
        for attr in my_attrs:
            self.assertEqual(attr in my_amenity.__dict__.keys(), True)

        # Checks for class attributes
        self.assertTrue(hasattr(my_amenity, 'name'))
        # Cheks if class attribute is a empty string
        self.assertEqual(getattr(my_amenity, 'name'), "")

        # Checks that some falses attributes
        my_attrs = ['name', 'create_time', 'update_time']
        for attr in my_attrs:
            self.assertEqual(attr in my_amenity.__dict__.keys(), False)

    def test_unique_id(self):
        """
        Checks for a unique id
        """
        # Checks if two instances has diferents id
        my_amenity = Amenity()
        my_amenity_2 = Amenity()
        self.assertNotEqual(my_amenity.id, my_amenity_2.id)

    def test_datetime(self):
        """
        Checks for datetime attributes
        """
        #Test if two instnace has diferent datetime
        my_amenity = Amenity()
        my_amenity_2 = Amenity()
        self.assertNotEqual(my_amenity.created_at, my_amenity_2.created_at)
        self.assertNotEqual(my_amenity.updated_at, my_amenity_2.updated_at)

        # Test if attribute created_at and updated_at are datetime instance
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity.created_at, datetime.datetime)
        self.assertIsInstance(my_amenity.updated_at, datetime.datetime)

    def test_UUID4(self):
        """
        Checks for the ID generation protocol
        """
        # Checks that the ID generated is the version 4
        my_amenity = Amenity()
        version = uuid.UUID(my_amenity.id).version
        self.assertEqual(version, 4)

    def test_created_and_updated_at(self):
        """
        Checks if updated_t attribute changes when a new attribute is
        added to the object and created_at is the same all the time.
        """
        # Checks that updated_at changes
        my_amenity = Amenity()
        updated_1 = str(my_amenity.updated_at)
        my_amenity.name = "New York"
        my_amenity.save()
        updated_2 = str(my_amenity.updated_at)
        self.assertNotEqual(updated_1, updated_2)

        # Checks that created_at doesn't change
        my_amenity = Amenity()
        created_1 = str(my_amenity.created_at)
        my_amenity.name = "Chicago"
        my_amenity.save()
        created_2 = str(my_amenity.created_at)
        self.assertEqual(created_1, created_2)

    def test_add_new_attributes(self):
        """
        Checks that can add new attributes to the objects
        """
        # Checks new attributes are added
        dict_attr = {'name': 'Betty', 'last': 'Holberton', 'age': 40}
        my_amenity = Amenity()
        for key, value in dict_attr.items():
            setattr(my_amenity, key, value)
        for key, value in dict_attr.items():
            self.assertTrue(hasattr(my_amenity, key))
            self.assertEqual(getattr(my_amenity, key), value)

        # Checks for all attributes for the object
        my_attrs = ['id', 'created_at', 'updated_at', 'name', 'last', 'age']
        for attr in my_attrs:
            self.assertEqual(attr in my_amenity.__dict__.keys(), True)

    def test_str_method(self):
        """
        Checks str method
        """
        my_amenity = Amenity()
        string = "[{}] ({}) {}".format(my_amenity.__class__.__name__, my_amenity.id,
                                       my_amenity.__dict__)
        self.assertEqual(str(my_amenity), string)

    def test_to_dict_method(self):
        """
        Checks dict method
        """
        # Checks if it convert to a dict type
        my_amenity = Amenity()
        my_amenity.name = "Holberton"
        my_amenity.my_number = 89
        my_amenity.my_float = 100.54
        my_amenity.my_list = ["Hello", "world", 100]
        my_amenity.my_dict = {'name': 'Betty', 'last_name': 'Holberton', 'age': 85}
        my_amenity.save()
        my_amenity_json = my_amenity.to_dict()
        # checks if the method really convert to a dict type all the attributes
        self.assertEqual(type(my_amenity_json), dict)
        for key, value in my_amenity_json.items():
            # checks if the dict has the same attributes keys that the object
            self.assertTrue(hasattr(my_amenity, key))
            # checks if datetime was safe as a iso format and its type
            if key == "created_at" or key == "updated_at":
                _datetime = getattr(my_amenity, key).isoformat()
                self.assertEqual(_datetime, value)
                self.assertTrue(type(value) == str)
            # checks the class name attribute and its type
            elif key == "__class__":
                self.assertEqual(my_amenity.__class__.__name__, value)
                self.assertTrue(type(value) == str)
            else:
                #checks the value for others attributes
                self.assertEqual(getattr(my_amenity, key), value)
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
        my_amenity = Amenity()
        my_amenity.name = "Holberton"
        my_amenity.my_number = 89
        my_amenity_json = my_amenity.to_dict()
        my_new_my_amenity = Amenity(**my_amenity_json)
        # Checks that the object has the same attributes that the my_amenity
        dict_attr = {'name': 'Holberton', 'my_number': 89, 'id': my_amenity.id,
                     'created_at': my_amenity.created_at,
                     'updated_at': my_amenity.updated_at}
        for key, value in dict_attr.items():
            self.assertTrue(hasattr(my_new_my_amenity, key))
            self.assertEqual(getattr(my_new_my_amenity, key), value)
        # Checks if __class__ attribute was not added
        self.assertTrue(hasattr(my_new_my_amenity, key))
        cls_name = getattr(my_new_my_amenity, key)
        self.assertNotEqual(cls_name, my_amenity_json["__class__"])
