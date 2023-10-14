#!/usr/bin/python3
"""test for the Place class"""


from models.place import Place
from unittest import TestCase


class TestPlace(TestCase):
    """TestPlace class"""
    def test_create(self):
        """Unittest for creation of a Place"""
        Place()
