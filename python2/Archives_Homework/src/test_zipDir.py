import zipDir
import unittest
import os
#import time
import shutil
import zipfile

class TestZipDir(unittest.TestCase):
    
    def setUp(self):
        self.cwd = os.getcwd()
        self.topdir = "workspace"  # can be anywhere
        self.mount = "v:\\"
        self.targdir = self.mount + self.topdir
        self.dir = "zipdir_test"
        self.path = os.path.join(self.targdir, "zipdir_test")
        self.files = ["batman.txt", "chalupa.dat", "spam.foo"]
        self.subdir = "eggs_dir"
        self.zipfile = self.dir + ".zip"  # keep in cwd
        os.mkdir(self.path)
        os.mkdir(os.path.join(self.path,self.subdir))
        self.expected = []
        for fn in self.files:
            fh = open(os.path.join(self.path,fn), "w")
            fh.close()
            self.expected.append(self.dir + "/" + fn)
            # time.sleep(1)  not necessary
        #print(self.expected)
        
    def test_zipDir(self):
        zipDir.zipDir(self.path) # note change
        zf = zipfile.ZipFile(self.zipfile, "r")            
        zf.close()
        # order doesn't matter so compare sets (safer)
        self.assertEqual(set(zf.namelist()), set(self.expected))
            
    def tearDown(self):
        os.unlink(self.zipfile)
        os.chdir(self.cwd)
        shutil.rmtree(self.path) # I never ignore errors
    
if __name__ == "__main__":
    unittest.main()
