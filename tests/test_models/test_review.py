#!/usr/bin/python3
"""
Unittest module for Review Class
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import pycodestyle


class test_review(test_basemodel):
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
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        Validate instance.place_id is str
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Validate instance.user_id is str
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Validate instance.text is str
        """
        new = self.value()
        self.assertEqual(type(new.text), str)

    @classmethod
    def setUpClass(cls):
        """
        Test
        """
        print('\n****************** Init Testing ******************\n')
        cls.my_Review = Review()

    def test_is_an_instance(self):
        """
        Instantiating Reviews
        """
        my_Review = Review()
        self.assertIsInstance(my_Review, Review)

    def test_type_instance(self):
        """
        type instance
        """
        self.assertIs(type(self.my_Review.place_id), str)
        self.assertIs(type(self.my_Review.user_id), str)
        self.assertIs(type(self.my_Review.text), str)

    def test_attributes(self):
        """
        Test Attributes
        """
        self.assertTrue(hasattr(Review, "__init__"))
        self.assertTrue(hasattr(Review, "__str__"))
        self.assertTrue(Review, "place_id")
        self.assertTrue(Review, "user_id")
        self.assertTrue(Review, "text")

    def test_pycodestyle(self):
        """
        Test style PEP8.
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "code style errors")

    @classmethod
    def tearDownClass(cls):
        """
        Test
        """
        print('\n****************** Finish Testing ******************\n')
