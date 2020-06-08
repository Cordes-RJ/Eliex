# -*- coding: utf-8 -*-

import os

# Get Extension of file from filepath string 
def getExt(filepath):
    i = filepath.rindex(".")
    return filepath[i:len(filepath)]

"""
print(getExt("testfolder\test.txt"))
"""

# Rename file
def renameFile(filepath, name):
    os.rename(filepath)