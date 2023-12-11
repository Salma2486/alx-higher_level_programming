#!/usr/bin/python3
import unittest
import os
from models.base import Base

class TestBase(unittest.TestCase):

    def test_init(self):
        obj1 = Base()

        self.assertEqual(obj1.id, 1)

if __name__ == '__main__':
    unittest.main()
