#!/usr/bin/python3
"""Defines a unittest module for database engine."""
import unittest
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import storage
import os
from os import getenv

@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'DB')
class TestDBStorage(unittest.TestCase):
    """Class that tests database storage methods."""
    
   pass 
