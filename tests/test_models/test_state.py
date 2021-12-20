#!/usr/bin/python3
"""
Unittest module for State Class
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


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

    def test_name3(self):
        """Test State has attr name"""

        new = self.value()
        self.assertEqual(type(new.name), str)
