'''
Created on Feb 17, 2015

@author: tmougham
'''
import unittest
from match_v_search import check_number

p1 = """While I was at the store in Washington, DC 20001 I tried to call 555-123-4567 on my mobile
but accidentally called 555-754-4321.  The person on the line redirected me to 
999-999-9999 which I don't think is a real number. Neither is 000-000-0000 or 555-555-0000.
Well, I will try (555) 123-4567 again now."""

p1a = """While I was at the store in Washington, DC 20001 I tried to call (555) 123-4567 on my mobile
but accidentally called (555)-754-4321.  The person on the line redirected me to 
(999)-999-9999 which I don't think is a real number. Neither is (000)-000-0000 or (555) 555-0000.
Well, I will try (555) 123-4567 again now."""


p2 = "555-555-5555"
p2a = "(555)-555-5555"


p3 = "What is the author's phone number?"


class Test(unittest.TestCase):


    def test_match(self):
        #result = check_number(p2)
        #self.assertEqual("555-555-5555", result)
        self.assertEqual("555-555-5555", check_number(p2))
        self.assertEqual("(555)-555-5555", check_number(p2a))


    def test_search(self):
        #result = check_number(p1)
        #self.assertEqual(305, result)
        self.assertEqual(305, check_number(p1))
        self.assertEqual(315, check_number(p1a))
     
        
    def test_none(self):
        result = check_number(p3)
        self.assertIsNone(result)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()