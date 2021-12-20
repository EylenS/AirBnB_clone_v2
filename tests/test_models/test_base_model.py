#!/usr/bin/python3
"""
Unittest module for Base Class
"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pycodestyle


class test_basemodel(unittest.TestCase):
    """
    In this test we are testing Base class
    creating new instance from class and
    validate its attributes
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        SetUp method
        """
        pass

    def tearDown(self):
        """
        TearDown method
        """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """
        Testing class model
        """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """
        Creatign instance fomr kwargs
        """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        Testing update values from kwargs
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """
        Testing save
        """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        Testing __str__ instance thunder method
        """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """
        Testing to_dict() instance method
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """
        Testing add attributes to instance from kwargs
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """
        Add attributes from kwargs
        """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """
        Validate type id is str
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """
        Validate datetime format
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    @classmethod
    def setUpClass(cls):
        """
        Init testing enviroment
        """
        print('\n****************** Init Testing ******************\n')
        ...

    def test_is_an_instance(self):
        """
        Instantiating BaseModels
        """
        my_BaseModel = BaseModel()
        self.assertIsInstance(my_BaseModel, BaseModel)

    def test_attributes(self):
        """
        Check if the class had corrects attributes
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_id(self):
        """
        Check if the class had unique id's
        """
        my_BaseModel = BaseModel().id
        my_1BaseModel = BaseModel().id
        self.assertNotEqual(my_BaseModel, my_1BaseModel)

    def test_save(self):
        """
        Check if the class save the update the date
        """
        my_BaseModel = BaseModel()
        my_1BaseModel = my_BaseModel.updated_at
        my_BaseModel.save()
        my_2BaseModel = my_BaseModel.updated_at
        self.assertNotEqual(my_1BaseModel, my_2BaseModel)

    def test_to_dict(self):
        """
        Test to dict
        """
        my_BaseModel = BaseModel()
        my_dict = my_BaseModel.to_dict()
        self.assertIs(type(my_dict), dict)
        self.assertIs(type(my_dict['created_at']), str)
        self.assertIs(type(my_dict['updated_at']), str)

    def test_style(self):
        """
        Check if the file had correct style
        """
        pstyle = pycodestyle.StyleGuide(quiet=True)
        result = pstyle.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors.")

    @classmethod
    def tearDownClass(cls):
        """
        Clear testing enviroment
        """
        print('\n****************** Finish Testing ******************\n')
        ...
