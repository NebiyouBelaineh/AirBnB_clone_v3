#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        # self.assertEqual(result.total_errors, 0,
        #                  "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """setup class variables"""
        cls.storage = DBStorage()

    def setUp(self):
        """setup the variables before method testing"""
        self.storage.reload()

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get(self):
        """Test get method"""
        # Create a User object and add it to the database
        user1 = User(email="bod.marley@gmail.com",
                     password="8795",
                     first_name="Bob",
                     last_name="Marley")
        self.storage.new(user1)
        self.storage.save()

        # Retrieve the user object using get method
        retrieved_user = self.storage.get(User, user1.id)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, "bod.marley@gmail.com")

        # Test get method with non-existent ID
        non_existent_user = self.storage.get(User, "non_existent_id")
        self.assertIsNone(non_existent_user)
        self.storage.delete(user1)
        self.storage.save()

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count(self):
        """Test count method"""
        # Count the number of User objects before adding any
        initial_count = self.storage.count(User)

        # Create and add User objects to the database
        user1 = User(email="dridi.mohamed@gmail.com",
                     password="88745",
                     first_name="Dridi",
                     last_name="Mohamed")
        user2 = User(email="nebiyou.belaineh@gmail.com",
                     password="546",
                     first_name="Belaineh",
                     last_name="Nebiyou")
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.save()

        # Count the number of User objects after adding
        updated_count = self.storage.count(User)
        self.assertEqual(updated_count, initial_count + 2)
        self.storage.delete(user1)
        self.storage.delete(user2)
        self.storage.save()
