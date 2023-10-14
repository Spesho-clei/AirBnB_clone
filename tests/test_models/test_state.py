#!/usr/bin/python3
"""test for the State class"""


from models.state import State
from unittest import TestCase


class State(TestCase):
    """The State class"""
    def test_create(self):
        """Unittest for creation of a State"""
        State()
