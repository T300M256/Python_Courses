"""this test use of unittesting"""

import unittest

def title(s):
    "How close is this function to str.titl()?"
    #return s[0].upper()+s[1:]
    n = []
    for w in s.split():
        n.append(w.capitalize())
    return " ".join(n)

class TestTitle(unittest.TestCase):
    
    def test_against_title(self):
        self.assertEqual(title("the sun also rises"), "the sun also rises".title(), "The title function does not match the native string title method")
        
if __name__ == "__main__":
    unittest.main()