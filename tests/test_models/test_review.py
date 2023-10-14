#!/usr/bin/python3
"""test for the Review class"""


from models.review import Review
from unittest import TestCase


class TestReview(TestCase):
    """TestReview class"""
    def test_create(self):
        """Unittest for creation of a Review"""
        Review()
