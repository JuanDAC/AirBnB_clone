#!/usr/bin/python3
"""Unittest for state
"""


import unittest
from models.base_model import BaseModel
from models.place import Place
import os
import uuid
import datetime
from models.engine.file_storage import FileStorage
from models import storage


class Test_Place_class(unittest.TestCase):
    """
    Defines a class to evaluate diferent test cases for place
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
        my_place = Place()
        self.assertIsInstance(my_place, Place)
        self.assertIsInstance(my_place, BaseModel)
        self.assertFalse(type(my_place) == type(Place))
        self.assertFalse(id(my_place) == id(Place))
        my_place_2 = Place()
        self.assertTrue(type(my_place) == type(my_place_2))
        self.assertFalse(id(my_place) == id(my_place_2))

    def test_instances_attributes(self):
        """
        Checks attributes created to the new object
        """
        # Checks that base attributes are created for the object
        my_place = Place()
        my_attrs = ['id', 'created_at', 'updated_at']
        for attr in my_attrs:
            self.assertEqual(attr in my_place.__dict__.keys(), True)

        # Checks for class attributes
        self.assertTrue(hasattr(my_place, 'city_id'))
        self.assertTrue(hasattr(my_place, 'user_id'))
        self.assertTrue(hasattr(my_place, 'name'))
        self.assertTrue(hasattr(my_place, 'description'))
        self.assertTrue(hasattr(my_place, 'number_rooms'))
        self.assertTrue(hasattr(my_place, 'number_bathrooms'))
        self.assertTrue(hasattr(my_place, 'max_guest'))
        self.assertTrue(hasattr(my_place, 'price_by_night'))
        self.assertTrue(hasattr(my_place, 'latitude'))
        self.assertTrue(hasattr(my_place, 'longitude'))
        self.assertTrue(hasattr(my_place, 'amenity_ids'))
        # Cheks if class attribute is a empty string
        self.assertEqual(getattr(my_place, 'city_id'), "")
        self.assertEqual(getattr(my_place, 'user_id'), "")
        self.assertEqual(getattr(my_place, 'name'), "")
        self.assertEqual(getattr(my_place, 'description'), "")
        self.assertEqual(getattr(my_place, 'number_rooms'), 0)
        self.assertEqual(getattr(my_place, 'number_bathrooms'), 0)
        self.assertEqual(getattr(my_place, 'max_guest'), 0)
        self.assertEqual(getattr(my_place, 'price_by_night'), 0)
        self.assertEqual(getattr(my_place, 'latitude'), 0.0)
        self.assertEqual(getattr(my_place, 'longitude'), 0.0)
        self.assertEqual(getattr(my_place, 'amenity_ids'), [])

        # Checks that some falses attributes
        my_attrs = ['name', 'create_time', 'update_time']
        for attr in my_attrs:
            self.assertEqual(attr in my_place.__dict__.keys(), False)

    def test_unique_id(self):
        """
        Checks for a unique id
        """
        # Checks if two instances has diferents id
        my_place = Place()
        my_place_2 = Place()
        self.assertNotEqual(my_place.id, my_place_2.id)

    def test_datetime(self):
        """
        Checks for datetime attributes
        """
        #Test if two instnace has diferent datetime
        my_place = Place()
        my_place_2 = Place()
        self.assertNotEqual(my_place.created_at, my_place_2.created_at)
        self.assertNotEqual(my_place.updated_at, my_place_2.updated_at)

        # Test if attribute created_at and updated_at are datetime instance
        my_place = Place()
        self.assertIsInstance(my_place.created_at, datetime.datetime)
        self.assertIsInstance(my_place.updated_at, datetime.datetime)

    def test_UUID4(self):
        """
        Checks for the ID generation protocol
        """
        # Checks that the ID generated is the version 4
        my_place = Place()
        version = uuid.UUID(my_place.id).version
        self.assertEqual(version, 4)

    def test_created_and_updated_at(self):
        """
        Checks if updated_t attribute changes when a new attribute is
        added to the object and created_at is the same all the time.
        """
        # Checks that updated_at changes
        my_place = Place()
        updated_1 = str(my_place.updated_at)
        my_place.name = "New York"
        my_place.save()
        updated_2 = str(my_place.updated_at)
        self.assertNotEqual(updated_1, updated_2)

        # Checks that created_at doesn't change
        my_place = Place()
        created_1 = str(my_place.created_at)
        my_place.name = "Chicago"
        my_place.save()
        created_2 = str(my_place.created_at)
        self.assertEqual(created_1, created_2)

    def test_add_new_attributes(self):
        """
        Checks that can add new attributes to the objects
        """
        # Checks new attributes are added
        dict_attr = {'name': 'Betty', 'last': 'Holberton', 'age': 40}
        my_place = Place()
        for key, value in dict_attr.items():
            setattr(my_place, key, value)
        for key, value in dict_attr.items():
            self.assertTrue(hasattr(my_place, key))
            self.assertEqual(getattr(my_place, key), value)

        # Checks for all attributes for the object
        my_attrs = ['id', 'created_at', 'updated_at', 'name', 'last', 'age']
        for attr in my_attrs:
            self.assertEqual(attr in my_place.__dict__.keys(), True)

    def test_str_method(self):
        """
        Checks str method
        """
        my_place = Place()
        string = "[{}] ({}) {}".format(my_place.__class__.__name__, my_place.id,
                                       my_place.__dict__)
        self.assertEqual(str(my_place), string)

    def test_to_dict_method(self):
        """
        Checks dict method
        """
        # Checks if it convert to a dict type
        my_place = Place()
        my_place.name = "Holberton"
        my_place.my_number = 89
        my_place.my_float = 100.54
        my_place.my_list = ["Hello", "world", 100]
        my_place.my_dict = {'name': 'Betty', 'last_name': 'Holberton', 'age': 85}
        my_place.save()
        my_place_json = my_place.to_dict()
        # checks if the method really convert to a dict type all the attributes
        self.assertEqual(type(my_place_json), dict)
        for key, value in my_place_json.items():
            # checks if the dict has the same attributes keys that the object
            self.assertTrue(hasattr(my_place, key))
            # checks if datetime was safe as a iso format and its type
            if key == "created_at" or key == "updated_at":
                _datetime = getattr(my_place, key).isoformat()
                self.assertEqual(_datetime, value)
                self.assertTrue(type(value) == str)
            # checks the class name attribute and its type
            elif key == "__class__":
                self.assertEqual(my_place.__class__.__name__, value)
                self.assertTrue(type(value) == str)
            else:
                #checks the value for others attributes
                self.assertEqual(getattr(my_place, key), value)
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
        my_place = Place()
        my_place.name = "Holberton"
        my_place.my_number = 89
        my_place_json = my_place.to_dict()
        my_new_my_place = Place(**my_place_json)
        # Checks that the object has the same attributes that the my_place
        dict_attr = {'name': 'Holberton', 'my_number': 89, 'id': my_place.id,
                     'created_at': my_place.created_at,
                     'updated_at': my_place.updated_at}
        for key, value in dict_attr.items():
            self.assertTrue(hasattr(my_new_my_place, key))
            self.assertEqual(getattr(my_new_my_place, key), value)
        # Checks if __class__ attribute was not added
        self.assertTrue(hasattr(my_new_my_place, key))
        cls_name = getattr(my_new_my_place, key)
        self.assertNotEqual(cls_name, my_place_json["__class__"])
