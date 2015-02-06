import unittest
import filecount
import glob
import time
import os

PATHSTEM = "v:\\workspace\\FileHandling\\src\\testfc\\"
#PATHSTEM = "."

class TestFilecount(unittest.TestCase):
    
    def setUp(self):
        self.path = PATHSTEM
        self.files = ["batman.txt", "chalupa.txt", "spam.out", "eggs.bat"]
        self.dir = "foo.bar"
        self.expected_count = {'.txt':2, '.bat': 1, '.out': 1}
        os.mkdir(self.path)
        for fn in self.files:
            f = open(self.path+fn, "w")
            f.close()
            time.sleep(1)
        os.mkdir(self.path+self.dir)
    
    def test_count_expected(self):
        """new test...see if the file counts match what should be expected from out list"""
        fc = filecount.count_by_ext(path=self.path)
        self.assertEqual(fc,self.expected_count,msg="The counts returned by function do not match expected")
 
    def tearDown(self):
        os.rmdir(self.path+self.dir)
        for fn in self.files:
            os.unlink(self.path+fn)
        os.rmdir(self.path)

if __name__ == "__main__":
    unittest.main()
        
    