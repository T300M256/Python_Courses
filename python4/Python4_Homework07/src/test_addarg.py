'''
Created on Jun 15, 2015

@author: tmougham
'''
import unittest
from addarg import addarg

class Test(unittest.TestCase):


    def test_addarg(self):
        @addarg(1)
        def pargs(*args, **kw):
            return args
        self.assertEqual((1,2,3), pargs(2,3))
        self.assertEqual((1,'child'), pargs("child"))
        
    def test_addarg_keyword(self):
        @addarg(1)
        def pargs_kwargs(*args, **kw):
            return(args, kw)
        self.assertEqual(((1,'child'),{'foo':'bar'}), pargs_kwargs("child",foo="bar"))

        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_addarg']
    unittest.main()