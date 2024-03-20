#!/usr/bin/python3
"""Defines a unittest module for database engine."""
import unittest
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import storage
from models.engine.db_storage import DBStorage
import os
from os import getenv

@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'DB')
class TestDBStorage(unittest.TestCase):
    """Tests for the database engine."""

    @patch('sqlalchemy.create_engine')
    @patch('sqlalchemy.orm.sessionmaker')
    def test_init(self, mock_sess, mock):
        fake_engine = MagicMock()
        mock.return_value = fake_engine

        mock_s = MagicMock()
        mock_sess.return_value = mock_s

        storage = DBStorage()

        mock.assert_called_once()
        mock_sess.assert_called_once()


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""

    @classmethod
    def setUp(cls):
        """Prepare for the documentation tests."""
        cls.funcs = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_function_docs(self):
        """Test that all functions have documentation."""
        for func_name, func in self.funcs:
            self.assertIsNotNone(func.__doc__, f"{func_name} lacks documentation")

        def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_pep8_conformance_db_storage(self):
        """Test if db_storage.py conformant to PEP8."""
        pep = pycodestyle.StyleGuide(quiet=True)
        result = pep.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
            """Test tests/test_models/test_db_storage.py conforms to PEP8."""
            pep8s = pycodestyle.StyleGuide(quiet=True)
            result = pep8s.check_files(['tests/test_models/test_engine/\
    test_db_storage.py'])
            self.assertEqual(result.total_errors, 0,
                             "Found code style errors (and warnings).")

    def test_funcsunc_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.funcs:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0])) 
