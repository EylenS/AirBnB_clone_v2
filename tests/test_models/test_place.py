#!/usr/bin/python3
"""
Unittest module for Place Class
"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import pycodestyle


class test_Place(test_basemodel):
    """
    In this test we are testing Place class
    creating new instance from class and
    validate its attributes
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Validate type instance.city_id is str
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Validate type instance.user_id is str
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        Validate type instance.name is str
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        Validate type instance.description is str
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        Validate type instance.number_rooms is int
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Validate type instance.number_bathrooms is int
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        Validate type instance.max_guest is int
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        Validate type instance.price_by_night is int
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        Validate type instance.latitude is float
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Validate type instance.longitude is float
        """
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """
        Validate type instance.amenity_ids is list
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    @classmethod
    def setUpClass(cls):
        """
        Test
        """

        print('\n****************** Init Testing ******************\n')
        cls.my_Place = Place()

    def test_is_an_instance(self):
        """
        Instantiating Places
        """
        my_Place = Place()
        self.assertIsInstance(my_Place, Place)

    def test_type_instance(self):
        """
        type instance
        """
        self.assertIs(type(self.my_Place.city_id), str)
        self.assertIs(type(self.my_Place.user_id), str)
        self.assertIs(type(self.my_Place.name), str)
        self.assertIs(type(self.my_Place.description), str)
        self.assertIs(type(self.my_Place.number_rooms), int)
        self.assertIs(type(self.my_Place.number_bathrooms), int)
        self.assertIs(type(self.my_Place.max_guest), int)
        self.assertIs(type(self.my_Place.price_by_night), int)
        self.assertIs(type(self.my_Place.latitude), float)
        self.assertIs(type(self.my_Place.longitude), float)
        self.assertIs(type(self.my_Place.amenity_ids), list)

    def test_attributes(self):
        """
        Test Attributes
        """

        self.assertTrue(hasattr(Place, "__init__"))
        self.assertTrue(hasattr(Place, "__str__"))
        self.assertTrue(Place, "name")
        self.assertTrue(Place, "description")
        self.assertTrue(Place, "number_rooms")
        self.assertTrue(Place, "number_bathrooms")
        self.assertTrue(Place, "max_guest")
        self.assertTrue(Place, "price_by_night")
        self.assertTrue(Place, "latitude")
        self.assertTrue(Place, "amenity_ids")

    def test_pycodestyle(self):
        """
        Test style PEP8.
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "code style errors")

    @classmethod
    def tearDownClass(cls):
        """
        Test
        """

        print('\n****************** Finish Testing ******************\n')
