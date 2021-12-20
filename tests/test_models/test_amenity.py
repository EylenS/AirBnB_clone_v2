#!/usr/bin/python3
"""
Unittest module for Amenity Class
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pycodestyle


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

    @classmethod
    def setUpClass(cls):
        """
        Test
        """
        print('\n****************** Init Testing ******************\n')
        cls.my_Amenity = Amenity()

    def test_name2(self):
        """
        Testing instance attribute `name`
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_is_an_instance(self):
        """
        Instantiating Amenitys
        """
        my_Amenity = Amenity()
        self.assertIsInstance(my_Amenity, Amenity)

    def test_type_instance(self):
        """
        type instance
        """
        self.assertIs(type(self.my_Amenity.name), str)

    def test_attributes(self):
        """
        Teste Atributes
        """
        self.assertTrue(hasattr(Amenity, "__init__"))
        self.assertTrue(hasattr(Amenity, "__str__"))
        self.assertTrue(Amenity, "name")

    def test_pycodestyle(self):
        """
        Test style PEP8.
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "code style errors")
