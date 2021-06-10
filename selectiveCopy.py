#!usr/bin/env python3
# Usage
# selectiveCopy.py <folder> <extension>

import os
import sys

def selectiveCopy(folder, fileExt):
    # TODO: Walk through folder, check extension
    for folder, subfolder, file in os.walk(os.path):
# TODO: Move specific files to new folder


if __name__ == "__main__":
    folder = sys.argv[1]
    fileExt = sys.argv[2]

    selectiveCopy(folder,fileExt)