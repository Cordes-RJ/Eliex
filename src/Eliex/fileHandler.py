# -*- coding: utf-8 -*-

import os

# Get Extension of file from filepath string 
def getExt(filepath):
    i = filepath.rindex(".")
    return filepath[i:len(filepath)]

"""
print(getExt("testfolder\test.txt"))
"""

# editFilePath edits the filepath of a file at a given filepath
def editFilePath(filepath, newFilepath):
    os.rename(filepath, newFilepath)

"""
renameFile("otherTest.txt", "testfolder\otherTest.pdf")
"""

# makeFile takes a string and creates a file given a filepath
def makeFile(filepath, string):
    with open(filepath,"a") as file:
        file.write(string)

