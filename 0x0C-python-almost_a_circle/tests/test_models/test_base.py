#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def test_create_instance_with_no_arguments(self):
        """ yred rt"""
        base = Base()
        self.assertEqual(base.id, 1)



if __name__ == "__main__":
    unittest.main()
