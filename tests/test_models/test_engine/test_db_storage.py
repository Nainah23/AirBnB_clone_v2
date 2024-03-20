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

@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db')
class TestDBStorage(unittest.TestCase):
    """Tests for the database engine."""

    def test_db_connection(self, mock_create_engine):
        """Test the database connection."""
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        storage = DBStorage()

        mock_create_engine.assert_called_once_with('mysql+mysqldb://{}:{}@{}/{}'
                                                   .format(os.getenv('HBNB_MYSQL_USER'),
                                                           os.getenv('HBNB_MYSQL_PWD'),
                                                           os.getenv('HBNB_MYSQL_HOST'),
                                                           os.getenv('HBNB_MYSQL_DB'),),
                                                   pool_pre_ping=True)


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db')
class TestDBStorageDocumentation(unittest.TestCase):
    """Tests to verify the documentation and style of DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the docstring tests."""
        cls.dbstorage_methods = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_method_docs(self):
        """Test that all methods are documented."""
        for method_name, method in self.dbstorage_methods:
            self.assertIsNotNone(method.__doc__, f"{method_name} is missing a docstring")

    def test_db_storage_module_docstring(self):
        """Test for the presence of a module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "The db_storage.py module needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "The db_storage.py module needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the presence of a class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "The DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "The DBStorage class needs a docstring")

    def test_pep8_compliance_db_storage(self):
        """Test that db_storage.py adheres to PEP8."""
        style_guide = pycodestyle.StyleGuide(quiet=True)
        result = style_guide.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_pep8_compliance_test_db_storage(self):
        """Test that tests/test_models/test_db_storage.py adheres to PEP8."""
        style_guide = pycodestyle.StyleGuide(quiet=True)
        result = style_guide.check_files(['tests/test_models/test_engine/test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors and warnings.")

    def test_method_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for method in self.dbstorage_methods:
            self.assertIsNot(method[1].__doc__, None,
                             f"The {method[0]} method needs a docstring")
            self.assertTrue(len(method[1].__doc__) >= 1,
                            f"The {method[0]} method needs a docstring")

