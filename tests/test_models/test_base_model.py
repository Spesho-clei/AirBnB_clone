#!/usr/bin/python3
"""This module defines a Unittest for BaseModel Class"""

from datetime import datetime
from models.base_model import BaseModel
from unittest import TestCase
from uuid import UUID

import re

class TestBaseModel(TestCase):
    """This is the TestBaseModel class"""

    def test_init(self):
        """Test initialization of BaseModel"""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.id, str)
        UUID(obj.id)

    def test_unique_ids(self):
        """Test uniqueness of generated ids"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj2.id, obj3.id)
        self.assertNotEqual(obj3.id, obj1.id)

    def test_init_with_args(self):
        """Test initialization of BaseModel with arguments"""
        obj1 = BaseModel('one')
        obj2 = BaseModel('arg', kw='two')
        obj3 = BaseModel(name='someone')
        self.assertTrue(hasattr(obj1, 'id'))
        self.assertIsNone(getattr(obj2, 'id', None))
        self.assertIsNone(getattr(obj3, 'id', None))

    def test_to_dict(self):
        """Test BaseModel to_dict method"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict.get('__class__'), 'BaseModel')

    def test_save(self):
        """Test if updated_at is updated after save()"""
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_repr(self):
        """Test string representation of BaseModel"""
        obj = BaseModel()
        pattern = r'^\[BaseModel\] \(\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\) \{.*\}$'
        self.assertTrue(re.match(pattern, str(obj)))
