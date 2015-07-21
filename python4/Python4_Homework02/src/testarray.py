"""
Test 3D array.
"""
import unittest
import arr

class TestArray(unittest.TestCase):
    def test_zeroes(self):
        for N in range(4):
            a = arr.array(N,N,N)
            for i in range(N):
                for j in range(N):
                    for z in range(N):
                        self.assertEqual(a[i,j,z], 0)
                    
    def test_identity(self):
        for N in range(4):
            a = arr.array(N,N,N)
            for i in range(N):
                a[i, i, i] = 1
            for i in range(N):
                for j in range(N):
                    for z in range(N):
                        self.assertEqual(a[i,j,z], i==j and i==z, "Not equal at i: %d j: %d z: %d N: %d" % (i,j,z, N))
                    
    def _index(self, a, r, c, z):
        return a[r,c,z]
    
    def test_key_validity(self):
        a = arr.array(10,10,10)
        self.assertRaises(KeyError, self._index, a, -1, 1, 1)
        self.assertRaises(KeyError, self._index, a, 10, 1, 1)
        self.assertRaises(KeyError, self._index, a, 1, -1, 1)
        self.assertRaises(KeyError, self._index, a, 1, 10, 1)
        self.assertRaises(KeyError, self._index, a, 1, 1, -1)
        self.assertRaises(KeyError, self._index, a, 1, 1, 10)

if __name__ == "__main__":
    unittest.main()