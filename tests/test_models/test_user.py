#!/usr/bin/python3
"""Test for the User class"""


from models.user import User
from unittest import TestCase


class TestUser(TestCase):
    """TestUser class"""
    def test_create(self):
        """Unittest for creation of a User"""
        User()
