#!/usr/bin/python3
"""
Unittest module for City Class
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pycodestyle


class test_City(test_basemodel):
    """
    In this test we are testing City class
    creating new instance from class and
    validate its attributes
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Validate type id is str
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Validate type instance.name is str
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @classmethod
    def setUpClass(cls):
        """
        Test
        """

        print('\n****************** Init Testing ******************\n')
        cls.my_City = City()

    def test_is_an_instance(self):
        """
        Instantiating Citys
        """
        my_City = City()
        self.assertIsInstance(my_City, City)

    def test_type_instance(self):
        """
        type instance
        """
        self.assertIs(type(self.my_City.state_id), str)
        self.assertIs(type(self.my_City.name), str)

    def test_attributes(self):
        """
        Test Attributes
        """

        self.assertTrue(hasattr(City, "__init__"))
        self.assertTrue(hasattr(City, "__str__"))
        self.assertTrue(City, "state_id")
        self.assertTrue(City, "name")

    def test_pycodestyle(self):
        """
        Test style PEP8.
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "code style errors")

    @classmethod
    def tearDownClass(cls):
        """
        Test
        """

        print('\n****************** Finish Testing ******************\n')
