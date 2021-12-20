#!/usr/bin/python3
"""Contains the TestUserDocs classes"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Test to check the documentation and style for User class."""

    def __init__(self, *args, **kwargs):
        """Test to check User class inherits from Basemodel"""

        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

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
