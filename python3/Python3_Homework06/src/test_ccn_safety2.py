'''
Created on Feb 18, 2015

@author: tmougham
'''
import unittest
import ccn_safety2

text = """Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number
that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and
security experts."""
text = text.replace("\n", " ")


safe = """Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? It is because a number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and security experts."""

class Test(unittest.TestCase):


    def test_clean_ccn(self):
        """verify that the function returns cleaned credit card numbers"""
        self.maxDiff = None
        self.assertEqual(safe, ccn_safety2.clean_ccn(text))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()