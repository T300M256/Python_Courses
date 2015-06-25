'''
Created on Feb 10, 2015

@author: tmougham
'''
import unittest
import coconuts


class Test(unittest.TestCase):
    
    def test_weights_differ(self):
        """
        verifies that each type of coconut has a different weight
        """
        #
        weights = set()
        weights.add(coconuts.SouthAsian().weight)
        weights.add(coconuts.MiddleEastern().weight)
        weights.add(coconuts.American().weight)
        self.assertEqual(3, len(weights))
    
    def test_bad_attribute(self):
        """
        verfies that an AttributeError is thrown when a string object is passes to add_coconut
        """
        i = coconuts.Inventory()
        self.assertRaises(AttributeError, i.add_coconut, "foobar")
        
    
    def test_total_weight(self):
        """
        verifies total weight works as expected
        """
        # add coconuts to inventory
        
        # note...need to correct his so we use the coconut types defined in the module
        
        inv = coconuts.Inventory()
        #for ctype, weight, count in (("South Asian", 3, 2),("Middle Eastern", 2.5, 1),("American", 3.5,3)):
        for cnut, count in ((coconuts.SouthAsian(), 2),(coconuts.MiddleEastern(), 1),(coconuts.American(),3)):
            for i in range(count):
                # create and add each coconut
                inv.add_coconut(cnut)
        # check total
        self.assertEqual(19, inv.total_weight())
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()