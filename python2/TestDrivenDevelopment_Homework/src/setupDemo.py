"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""

import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
        
    def test_1(self):
        "Verify creation of file is possible"
        files_to_create = set(("this.txt", "that.txt", "the_other.txt"))
        for filename in (files_to_create):
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        exist_files = set(os.listdir())
        self.assertEqual (exist_files, files_to_create, msg="There appear to be unexpected files in the directory:"+" ".join(exist_files.difference(files_to_create)))
            
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
 
    def test_3(self):
        "Verify creation of binary file of exact size is possible"
        fn = "test_binary.egg"
        num_bytes = 100000
        b = open(fn, "wb")
        milbytes = bytearray([1]*num_bytes)
        b.write(milbytes)
        b.close()
        actual_bytes = os.stat(fn).st_size
        self.assertEqual(actual_bytes, num_bytes, msg="Failed to created binary file of correct number of bytes")
        
        
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        
if __name__ == "__main__":
    unittest.main()