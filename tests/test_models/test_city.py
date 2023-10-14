#!/usr/bin/python3
"""test for the City class"""


from models.city import City
from unittest import TestCase


class TestCity(TestCase):
    """The TestCity class"""
    def test_create(self):
        """Unittest for creation of a City"""
        City()
