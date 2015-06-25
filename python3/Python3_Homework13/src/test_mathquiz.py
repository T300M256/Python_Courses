'''
Created on May 10, 2015

@author: tmougham
'''
import unittest
import mathquiz

class TestMathQuiz(unittest.TestCase):


    def test_get_ints(self):
        # test that get_ints returns a pair of ints
        # within the expected range
        the_max = 10
        n1, n2 = mathquiz.get_ints(the_max)
        
        self.assertGreaterEqual(n1,1,"first int is lower than minimum")
        self.assertGreaterEqual(n2,1,"second int is lower than minimum")
        self.assertLessEqual(n1,10,"first int is larger than max")
        self.assertLessEqual(n2,10,"second int is larger than max")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()