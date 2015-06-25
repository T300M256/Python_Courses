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
        # need to get a list or of the weights of each type and if the
        # number of unqiue values in the set is equal to the number of
        # types then we have different weights for each
        
        ine = coconuts.Inventory()
        
        # okay, apparently the sepeare Inventorys in each test are not
        # unqiue or rather not distince instances
        
        print("Bef Len of inventory",len(ine.coconuts))
        
        ine.add_coconut(coconuts.Coconut("South Asian",3))
        ine.add_coconut(coconuts.Coconut("Middle Eastern",2.5))
        ine.add_coconut(coconuts.Coconut("American",3.5))
        
        print("Aft Len of inventory",len(ine.coconuts))
        
        weights = set()
        for c in ine.coconuts:
            weights.add(c.weight)
        
        print(ine.coconuts)
        self.assertNotEqual(0,len(ine.coconuts), "There are no coconuts in the inventory")
        self.assertEqual(len(ine.coconuts), len(weights))
    
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
        inv = coconuts.Inventory()
        for ctype, weight, count in (("South Asian", 3, 2),("Middle Eastern", 2.5, 1),("American", 3.5,3)):
            for i in range(count):
                # create and add each coconut
                cnut = coconuts.Coconut(ctype, weight)
                inv.add_coconut(cnut)
        # check total
        self.assertEqual(19, inv.total_weight())
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()