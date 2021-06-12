#!/usr/bin/env python3
# Usage
# selectiveCopy.py <folder> <extension>

import os
import sys

def selectiveCopy(folder, fileExt):
    # Create new folder
    ext = fileExt.replace(".","")
    os.mkdir(folder+"\\{}_files".format(ext))
    #  Walk through folder, check extension
    for folder, subfolder, file in os.walk(os.path(folder)):
        for filename in file:
            if filename.endswith(fileExt):
                # Move specific files to new folder
                os.copy(os.path.abspath(filename),folder+"\\{}_files\\{}".format(fileExt,filename) )




if __name__ == "__main__":
    folder = sys.argv[1]
    fileExt = sys.argv[2]

    selectiveCopy(folder,fileExt)