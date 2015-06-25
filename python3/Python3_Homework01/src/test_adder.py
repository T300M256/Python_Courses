'''
Created on Feb 7, 2015

@author: tmougham
'''
import unittest
from adder import add

class Test(unittest.TestCase):


    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(5,5), 10)
        self.assertEqual(add(100,5), 105)
        self.assertEqual(add(100,-5), 95)
    
    def test_bad_input_raise(self):
        self.assertRaises(TypeError, add, -1.1, 3)
        self.assertRaises(TypeError, add, 1.0, 3)
        self.assertRaises(TypeError, add, 1, 't')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_add']
    unittest.main()