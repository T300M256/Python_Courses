'''
Created on Mar 26, 2015

@author: tmougham
'''
import unittest
from furnishings import *

exp_counter = """Beds: 1
Bookshelves: 0
Sofas: 1
Tables: 0
"""

class Test(unittest.TestCase):


    #def test_map_the_home(self):
    #    home = []
    #    home.append(Bed('Bedroom'))
    #    home.append(Sofa('Living Room'))
    #    mp = map_the_home(home)
    #    self.assertEqual(type(mp['Bedroom']), Bed, "Did not find a Bed object mapped to Bedroom")
    #    self.assertEqual(type(mp['Living Room']), Sofa, "Did not find a Sofa object mapped to Living Room")
        
    def test_counter(self):
        home = []
        home.append(Bed('Bedroom'))
        home.append(Sofa('Living Room'))
        self.assertEqual(exp_counter, counter(home), "Counter output does not match expected.")

    def test_map_mentor(self):
        self.home = []
        self.home.append(Bed('Bedroom'))
        self.home.append(Sofa('Living Room'))
        self.home.append(Table('Bedroom'))

        mapping = map_the_home(self.home)
        self.assertTrue(isinstance(mapping['Bedroom'][0], Bed))
        self.assertTrue(isinstance(mapping['Living Room'][0], Sofa))
        self.assertTrue(isinstance(mapping['Bedroom'][1], Table))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()