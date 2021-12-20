#!/usr/bin/python3
"""
Unittest module for State Class
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.base_model import BaseModel
import os
import pycodestyle


class test_state(test_basemodel):
    """
    In this test we are testing State class
    creating new instance from class and
    validate its attributes
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def setUp(self):
        """Sets up the testing environment"""

        self.state_1 = State()
        self.state_2 = State()
        self.state_2.name = "Risaralda"
        self.state_2.name = "Antioquia"

    def tearDown(self):
        """Tears down the testing environment."""
        del self.state_1
        del self.state_2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_name3(self):
        """Test State has attr name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_inheritance(self):
        """Review inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attr(self):
        """Checks that new instance has attributes."""

        self.assertIn("name", self.state_2.__dict__)
        self.assertEqual(self.state_2.name, "Antioquia")

    @classmethod
    def setUpClass(cls):
        """
        Test
        """
        print('\n****************** Init Testing ******************\n')
        cls.my_state = State()

    def test_is_an_instance(self):
        """
        Instantiating states
        """
        my_state = State()
        self.assertIsInstance(my_state, State)

    def test_type_instance(self):
        """
        type instance
        """
        self.assertIs(type(self.my_state.name), str)

    def test_attributes(self):
        self.assertTrue(hasattr(State, "__init__"))
        self.assertTrue(hasattr(State, "__str__"))
        self.assertTrue(State, "name")

    def test_pycodestyle(self):
        """
        Test style PEP8.
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "code style errors")

    @classmethod
    def tearDownClass(cls):
        """
        Test
        """
        print('\n****************** Finish Testing ******************\n')
