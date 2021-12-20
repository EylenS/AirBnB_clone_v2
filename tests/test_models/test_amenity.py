#!/usr/bin/python3
"""
Unittest module for Amenity Class
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    In this test we are testing Amenity class
    creating new instance from class and
    validate its attributes
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Testing instance attribute `name`
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
