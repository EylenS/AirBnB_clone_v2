#!/usr/bin/python3
"""Unittest for database storage."""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.db_storage import DBStorage

class TestDBStorage(unittest.TestCase):
    """Testing test DBStorage."""

    @classmethod
    def setUpClass(cls):
        """Set Up for test"""
        cls.user = User()
        cls.user.first_name = "Christian"
        cls.user.last_name = "Granada"
        cls.user.email = "hellobaby@holbertonschool.com"
        cls.storage = DBStorage()

    @classmethod
    def tearDownClass(cls):
        """Launched at the end"""
        del cls.user

    