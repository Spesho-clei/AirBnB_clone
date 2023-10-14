#!/usr/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        with patch('models.storage') as mock_storage:
            HBNBCommand().onecmd("create BaseModel")
            mock_storage.all.return_value = {}
            mock_storage.new.return_value = None
            mock_storage.save.return_value = None
            expected_output = "Missing class name\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        with patch('models.storage') as mock_storage:
            HBNBCommand().onecmd("show")
            expected_output = "** class name missing **\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

            mock_storage.all.return_value = {}
            HBNBCommand().onecmd("show BaseModel")
            expected_output = "** instance id missing **\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

            mock_storage.all.return_value = {'BaseModel.123': 'mock_instance'}
            HBNBCommand().onecmd("show BaseModel 123")
            expected_output = "mock_instance\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        with patch('models.storage') as mock_storage:
            HBNBCommand().onecmd("update")
            expected_output = "** class name missing **\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

            mock_storage.all.return_value = {}
            HBNBCommand().onecmd("update BaseModel")
            expected_output = "** instance id missing **\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

            mock_storage.all.return_value = {'BaseModel.123': 'mock_instance'}
            HBNBCommand().onecmd("update BaseModel 123")
            expected_output = "** attribute name missing **\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

            mock_storage.all.return_value = {'BaseModel.123': 'mock_instance'}
            HBNBCommand().onecmd("update BaseModel 123 attribute_name")
            expected_output = "** value missing **\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

            HBNBCommand().onecmd('update BaseModel 123 attribute_name "value"')
            expected_output = ""
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        with patch('models.storage') as mock_storage:
            HBNBCommand().onecmd("destroy")
            expected_output = "** class name missing **\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

            mock_storage.all.return_value = {}
            HBNBCommand().onecmd("destroy BaseModel")
            expected_output = "** instance id missing **\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

            mock_storage.all.return_value = {'BaseModel.123': 'mock_instance'}
            HBNBCommand().onecmd("destroy BaseModel 123")
            expected_output = ""
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        with patch('models.storage') as mock_storage:
            HBNBCommand().onecmd("all")
            expected_output = "[str(obj[1]) for obj in items.items()]\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

            mock_storage.all.return_value = {
                'BaseModel.123': 'mock_instance',
                'OtherModel.456': 'other_instance'
            }
            HBNBCommand().onecmd("all BaseModel")
            expected_output = "['mock_instance']\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

            HBNBCommand().onecmd("all UnknownModel")
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)
    def test_new_method(self):
        """
        Unittest for a hypothetical new method
        """
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd('new_method arg1 arg2')
            result = out.getvalue().strip()
            self.assertEqual("Result of new method", result)

    def test_additional_case(self):
        """
        Unittest for an additional case
        """
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd('additional_case arg')
            result = out.getvalue().strip()
            self.assertEqual("Result of additional case", result)

    def test_updated_method(self):
        """
        Unittest for a method with updated behavior
        """
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd('updated_method arg1 arg2')
            result = out.getvalue().strip()
            self.assertEqual("Updated result of method", result)
if __name__ == '__main__':
    unittest.main()
