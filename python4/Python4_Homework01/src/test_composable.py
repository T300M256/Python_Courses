"""
test_compasable.py performs simple tests of compasable function.
"""
import unittest
from composable import Composable

def reverse(s):
    "Reversse  a string using negative-stride sequencing"
    return s[::-1]

def square(x):
    "Multiplies a number by itself"
    return x*x

def power(x,y):
    "raise a number x to power y"
    return x**y

class ComposableTestCase(unittest.TestCase):

    def test_power(self):
        squarer = Composable(square)
        po = squarer ** 3
        self.assertEqual(po(2), square(square(square(2))))
        
    def test_inverse(self):
        reverser = Composable(reverse)
        nulltran = reverser ** 2
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(nulltran(s),s)
    
    def test_square(self):
        squarer = Composable(square)
        po4 = squarer ** 2
        for v, r in ((1, 1), (2,16), (3, 81)):
            self.assertEqual(po4(v), r)

    def test_exception(self):
        fc = Composable(square)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc
        with self.assertRaises(TypeError):
            po = fc ** 2.0
        with self.assertRaises(ValueError):
            po = fc ** -2
            
if __name__ == "__main__":
    unittest.main()