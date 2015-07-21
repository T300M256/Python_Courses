'''
Created on Jun 13, 2015

@author: tmougham
'''
import unittest
from myDict import  myDict


class Test(unittest.TestCase):


    def test_myDict(self):
        d = myDict("default")
        d["spam"] = "eggs"
        d["batman"] = "chalupah"
        self.assertEqual("eggs", d.__getitem__("spam"))
        self.assertEqual("default", d.__getitem__("foobar"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_myDict']
    unittest.main()