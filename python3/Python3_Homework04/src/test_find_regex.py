'''
Created on Feb 17, 2015

@author: tmougham
'''
import unittest
import find_regex

class Test(unittest.TestCase):

    def test_find_location(self):
        """
        Tests that the start and end are what is expected
        """
        self.assertEqual(231,find_regex.start(),"Start location is incorrect")
        self.assertEqual(250,find_regex.end(),"End location is incorrect")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_find_location']
    unittest.main()