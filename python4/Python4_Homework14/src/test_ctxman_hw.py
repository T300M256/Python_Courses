'''
Created on Jul 8, 2015

@author: tmougham
'''
import unittest
from ctxman_hw import ctxman

class Test(unittest.TestCase):
    
    def raise_key_error(self):
        with ctxman(raising=True) as cm:
            raise KeyError
        return("Complete")
    
    def raise_value_error(self):
        with ctxman(raising=True) as cm:
            raise ValueError
        return("Complete")
    
    def return_some_value(self):
        with ctxman(raising=True) as cm:
            return("Complete")

    def test_key_error(self):
        self.assertNotEqual("Complete", self.raise_key_error)
        self.assertRaises(KeyError, self.raise_key_error)
    
    def test_value_error(self):
        self.assertEqual("Complete", self.raise_value_error())  
        
    def test_do_something(self):
        self.assertEqual("Complete", self.return_some_value())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_key_error']
    unittest.main()