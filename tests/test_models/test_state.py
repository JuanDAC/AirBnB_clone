#!/usr/bin/python3
"""Unittest for state
"""


import unittest
from models.base_model import BaseModel
from models.state import State
import os
import uuid
import datetime
from models.engine.file_storage import FileStorage
from models import storage


class Test_Base_model(unittest.TestCase):
    """
    Defines a class to evaluate diferent test cases for base_model
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
        my_state = State()
        self.assertIsInstance(my_state, State)
        self.assertIsInstance(my_state, BaseModel)
        self.assertFalse(type(my_state) == type(State))
        self.assertFalse(id(my_state) == id(State))
        my_state_2 = State()
        self.assertTrue(type(my_state) == type(my_state_2))
        self.assertFalse(id(my_state) == id(my_state_2))

    def test_instances_attributes(self):
        """
        Checks attributes created to the new object
        """
        # Checks that base attributes are created for the object
        my_state = State()
        my_attrs = ['id', 'created_at', 'updated_at']
        for attr in my_attrs:
            self.assertEqual(attr in my_state.__dict__.keys(), True)

        # Checks for class attributes
        self.assertTrue(hasattr(my_state, 'name'))
        # Cheks if class attribute is a empty string
        self.assertEqual(getattr(my_state, 'name'), "")

        # Checks that some falses attributes
        my_attrs = ['name', 'create_time', 'update_time']
        for attr in my_attrs:
            self.assertEqual(attr in my_state.__dict__.keys(), False)

    def test_unique_id(self):
        """
        Checks for a unique id
        """
        # Checks if two instances has diferents id
        my_state = State()
        my_state_2 = State()
        self.assertNotEqual(my_state.id, my_state_2.id)

    def test_datetime(self):
        """
        Checks for datetime attributes
        """
        #Test if two instnace has diferent datetime
        my_state = State()
        my_state_2 = State()
        self.assertNotEqual(my_state.created_at, my_state_2.created_at)
        self.assertNotEqual(my_state.updated_at, my_state_2.updated_at)

        # Test if attribute created_at and updated_at are datetime instance
        my_state = State()
        self.assertIsInstance(my_state.created_at, datetime.datetime)
        self.assertIsInstance(my_state.updated_at, datetime.datetime)

    def test_UUID4(self):
        """
        Checks for the ID generation protocol
        """
        # Checks that the ID generated is the version 4
        my_state = State()
        version = uuid.UUID(my_state.id).version
        self.assertEqual(version, 4)

    def test_created_and_updated_at(self):
        """
        Checks if updated_t attribute changes when a new attribute is
        added to the object and created_at is the same all the time.
        """
        # Checks that updated_at changes
        my_state = State()
        updated_1 = str(my_state.updated_at)
        my_state.name = "New York"
        my_state.save()
        updated_2 = str(my_state.updated_at)
        self.assertNotEqual(updated_1, updated_2)

        # Checks that created_at doesn't change
        my_state = State()
        created_1 = str(my_state.created_at)
        my_state.name = "Chicago"
        my_state.save()
        created_2 = str(my_state.created_at)
        self.assertEqual(created_1, created_2)

    def test_add_new_attributes(self):
        """
        Checks that can add new attributes to the objects
        """
        # Checks new attributes are added
        dict_attr = {'name': 'Betty', 'last': 'Holberton', 'age': 40}
        my_state = State()
        for key, value in dict_attr.items():
            setattr(my_state, key, value)
        for key, value in dict_attr.items():
            self.assertTrue(hasattr(my_state, key))
            self.assertEqual(getattr(my_state, key), value)

        # Checks for all attributes for the object
        my_attrs = ['id', 'created_at', 'updated_at', 'name', 'last', 'age']
        for attr in my_attrs:
            self.assertEqual(attr in my_state.__dict__.keys(), True)

    def test_str_method(self):
        """
        Checks str method
        """
        my_state = State()
        string = "[{}] ({}) {}".format(my_state.__class__.__name__, my_state.id,
                                       my_state.__dict__)
        self.assertEqual(str(my_state), string)

    def test_to_dict_method(self):
        """
        Checks dict method
        """
        # Checks if it convert to a dict type
        my_state = State()
        my_state.name = "Holberton"
        my_state.my_number = 89
        my_state.my_float = 100.54
        my_state.my_list = ["Hello", "world", 100]
        my_state.my_dict = {'name': 'Betty', 'last_name': 'Holberton', 'age': 85}
        my_state.save()
        my_state_json = my_state.to_dict()
        # checks if the method really convert to a dict type all the attributes
        self.assertEqual(type(my_state_json), dict)
        for key, value in my_state_json.items():
            # checks if the dict has the same attributes keys that the object
            self.assertTrue(hasattr(my_state, key))
            # checks if datetime was safe as a iso format and its type
            if key == "created_at" or key == "updated_at":
                _datetime = getattr(my_state, key).isoformat()
                self.assertEqual(_datetime, value)
                self.assertTrue(type(value) == str)
            # checks the class name attribute and its type
            elif key == "__class__":
                self.assertEqual(my_state.__class__.__name__, value)
                self.assertTrue(type(value) == str)
            else:
                #checks the value for others attributes
                self.assertEqual(getattr(my_state, key), value)
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
        my_state = State()
        my_state.name = "Holberton"
        my_state.my_number = 89
        my_state_json = my_state.to_dict()
        my_new_my_state = State(**my_state_json)
        # Checks that the object has the same attributes that the my_state
        dict_attr = {'name': 'Holberton', 'my_number': 89, 'id': my_state.id,
                     'created_at': my_state.created_at,
                     'updated_at': my_state.updated_at}
        for key, value in dict_attr.items():
            self.assertTrue(hasattr(my_new_my_state, key))
            self.assertEqual(getattr(my_new_my_state, key), value)
        # Checks if __class__ attribute was not added
        self.assertTrue(hasattr(my_new_my_state, key))
        cls_name = getattr(my_new_my_state, key)
        self.assertNotEqual(cls_name, my_state_json["__class__"])
