'''
Created on Jun 3, 2015

@author: tmougham
'''
import unittest
import mytree

class Test(unittest.TestCase):


    def testMyTree(self):
        t = mytree.Tree("D")
        for c in "BJQKFAC":
            t.insert(c)
        self.assertEqual(['A', 'B', 'C', 'D', 'F', 'J', 'K', 'Q'],list(t.walk()))

     
    def testData(self):
        """see that the data argument works"""
        t = mytree.Tree("D", "spam and eggs")
        self.assertEqual(t.data, "spam and eggs")
    
    
    def testFind(self):
        t = mytree.Tree("D", "spam and eggs")
        for c in "BJQKFAC":
            t.insert(c, "blah")

        self.assertEqual(t.find('D'),"spam and eggs")
        self.assertEqual(t.find('Q'),"blah")
        self.assertRaises(KeyError, t.find, 'Z')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMyTree']
    unittest.main()