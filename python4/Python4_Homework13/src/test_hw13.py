'''
Created on Jun 28, 2015

@author: tmougham
'''
import unittest
from hw13 import sstr


class Test(unittest.TestCase):

    def test_operators(self):
        s1 = sstr("abcde")
        self.assertEqual(s1 << 0,'abcde')
        self.assertEqual(s1 >> 0, 'abcde')
        self.assertEqual(s1 << 2, 'cdeab')
        self.assertEqual(s1 >> 2, 'deabc')
        self.assertEqual(s1 >> 5, 'abcde')
        self.assertEqual((s1 >> 5) << 5 == 'abcde', True)
        
    def test_type(self):
        s1 = sstr("abcde")
        self.assertIsInstance(s1 << 1, sstr)
        self.assertIsInstance(s1 >> 1, sstr)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_operators']
    unittest.main()