#!/usr/bin/python3
"""
This module contains all unittest cases for
Base class
"""
import unittest
import pep8
from models.base import Base
from models.square import Square
import sys
from io import StringIO
import json
import os


class TestSquare(unittest.TestCase):
    """
    Class containing functions to run
    multiple tests
    """
    def setUp(self):
        """
        function to redirect stdout to check
        outpute of functions relying on print
        """
        sys.stdout = StringIO()

    def tearDown(self):
        """
        cleans everything up after running
        setup
        """
        sys.stdout = sys.__stdout__

    def test_pep8_model(self):
        """
        Tests for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/square.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """
        Tests for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_00_documentation(self):
        """
        Test to see if documentation is
        created and correct
        """
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(Square.__init__.__doc__)
        self.assertTrue(hasattr(Square, "size"))
        self.assertTrue(Square.size.__doc__)
        self.assertTrue(hasattr(Square, "x"))
        self.assertTrue(Square.x.__doc__)
        self.assertTrue(hasattr(Square, "y"))
        self.assertTrue(Square.y.__doc__)
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertTrue(Square.__str__.__doc__)
        self.assertTrue(hasattr(Square, "update"))
        self.assertTrue(Square.update.__doc__)
        self.assertTrue(hasattr(Square, "to_dictionary"))
        self.assertTrue(Square.to_dictionary.__doc__)

    def test_0_id(self):
        """
        Testng for id

