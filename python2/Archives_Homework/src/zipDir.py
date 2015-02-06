import glob
import os
import zipfile

def zipDir(path):
    dirname = os.path.basename(path)
    os.chdir(path)
    files = glob.glob("*")
    os.chdir(os.pardir)
    zf = zipfile.ZipFile(os.path.basename(path)+ ".zip", "w")  # <--  made ths one change, other changes will be needed
    for fn in files:
        if os.path.isfile(os.path.join(dirname,fn)):
            zf.write(os.path.join(dirname,fn))
    zf.close()