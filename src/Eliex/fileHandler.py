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
def editFilePath(filepath, newFilepath):
    os.rename(filepath, newFilepath)
    
"""
renameFile("otherTest.txt", "testfolder\otherTest.pdf")
"""