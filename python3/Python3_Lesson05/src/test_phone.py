'''
Created on Feb 17, 2015

@author: tmougham
'''
import unittest
from phone import get_phone, text


class Test(unittest.TestCase):


    def test_phone(self):
        numbers = get_phone(text)
        self.assertEqual(len(numbers), 5)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()