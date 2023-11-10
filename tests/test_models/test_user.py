#!/usr/bin/python3
"""Test user"""
import unittest
from models.base_model import BaseModel
from models.user import User
import inspect
from models import storage
import pep8


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDocs(unittest.TestCase):
    """Base model document tests"""

    @classmethod
    def setUpClass(cls):
        """Testing class"""
        cls.base_funcs = inspect.getmembers(User, inspect.isfunction)

    def test_module_docstring(self):
        """module docstring length"""
        self.assertTrue(len(User.__doc__) >= 1)

    def test_class_docstring(self):
        """Class docstring length"""
        self.assertTrue(len(User.__doc__) >= 1)


class Test_user(unittest.TestCase):
    """Tests the user module"""

    def test_class(self):
        """Test class"""
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertTrue(issubclass(User, BaseModel))

    def test_instance(self):
        our_user = User()
        self.assertEqual(our_user.email, "")
        self.assertEqual(our_user.password, "")
        self.assertEqual(our_user.first_name, "")
        self.assertEqual(our_user.last_name, "")
        self.assertTrue(isinstance(our_user, BaseModel))
