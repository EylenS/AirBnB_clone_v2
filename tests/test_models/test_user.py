#!/usr/bin/python3
"""Contains the TestUserDocs classes"""
from models.base_model import BaseModel
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os
import pycodestyle


class test_User(test_basemodel):
    """Test to check the documentation and style for User class."""

    def __init__(self, *args, **kwargs):
        """Test to check User class inherits from Basemodel"""

        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def setUp(self):
        """Sets up testing environment."""
        self.model = BaseModel()
        self.model_1 = BaseModel()

    def test_first_name(self):
        """Test User has attr first_name, and it is an empty string"""

        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test User has attr last_name, and it is an empty string"""

        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test User has attr test_email, and it is an empty string"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test User has attr password, and it is an empty string"""
        new = self.value()
        self.assertEqual(type(new.password), str)

    @classmethod
    def setUpClass(cls):
        """
        Test
        """
        print('\n****************** Init Testing ******************\n')
        cls.my_user = User()
        cls.my_user.first_name = "Betty"
        cls.my_user.last_name = "Bar"
        cls.my_user.email = "airbnb@mail.com"
        cls.my_user.password = "root"

    def test_is_an_instance(self):
        """
        Instantiating Users
        """
        my_user = User()
        self.assertIsInstance(my_user, User)

    def test_type_instance(self):
        """
        type instance
        """
        self.assertIs(type(self.my_user.first_name), str)
        self.assertIs(type(self.my_user.last_name), str)
        self.assertIs(type(self.my_user.email), str)
        self.assertIs(type(self.my_user.password), str)

    def test_attributes(self):
        """
        Test Attributes
        """
        self.assertTrue(hasattr(User, "__init__"))
        self.assertTrue(hasattr(User, "__str__"))
        self.assertTrue(User, "first_name")
        self.assertTrue(User, "last_name")
        self.assertTrue(User, "email")
        self.assertTrue(User, "password")

    def test_pycodestyle(self):
        """
        Test style PEP8.
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "code style errors")

    @classmethod
    def tearDownClass(cls):
        """
        Test
        """
        print('\n****************** Finish Testing ******************\n')
