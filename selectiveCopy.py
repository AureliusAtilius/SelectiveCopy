#!/usr/bin/env python3
# Usage
# selectiveCopy.py <folder path> <file extension>

import os
import shutil
import sys
from shutil import copyfile

def selectiveCopy(folder, fileExt):
    # Create new folder if it doesn't already exist
    ext = fileExt.replace(".","")
    newFolder=folder+"\\{}_files".format(ext)
    if not os.path.isdir(newFolder):
        os.mkdir(newFolder)
    #  Walk through folder, check extension
    for folders, subfolders, files in os.walk(folder):
        for filename in files:
            if filename.endswith(fileExt):
                # Copy specific files to new folder
                shutil.copyfile(folder+"\\"+filename,newFolder+"\\"+filename )




if __name__ == "__main__":
    folder = sys.argv[1]
    fileExt = sys.argv[2]
    
    selectiveCopy(folder,fileExt)