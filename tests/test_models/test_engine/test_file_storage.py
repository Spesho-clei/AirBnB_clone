#!/usr/bin/python3
"""test for the FileStorage Class"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from unittest import TestCase


class TestFileStorage(TestCase):
    """This is the TestFileStorage Class"""
    def setUp(self):
        """
        setUp for the test cases
        """
        self.storage = FileStorage()

    def tearDown(self) -> None:
        """
        tearDown after tests
        """
        self.storage.all().clear()
        self.storage.save()

    def test_all(self):
        """Unittest for storage.all()"""
        self.assertTrue(isinstance(self.storage.all(), dict))

    def test_new(self):
        """Unittest for storage.new()"""
        size = len(self.storage.all())
        self.storage.new(BaseModel())
        self.assertEqual(size + 1, len(self.storage.all()))

    def test_save(self):
        """Unittest for storage.save()"""
        self.storage.save()

    def test_reload(self):
        """Unittest for storage.reload()"""
        self.storage.new(BaseModel())
        self.storage.save()
        self.storage.all().clear()
        self.storage.reload()
        self.assertGreater(len(self.storage.all()), 0)
