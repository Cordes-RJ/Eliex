# -*- coding: utf-8 -*-

import os
import ntpath

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

# checkForFile checks if a file exists or not, returns a bool
def checkForFile(filepath):
    return os.path.exists(filepath)

# getFileName gets the base file name from a path
def getFileName(filepath):
    return ntpath.basename(filepath)
    
"""
print(getFileName("C:/Users/xyz/Documents/Code/Eliex/src/Eliex/testfolder/hashLib/9dd4e461268c8034f5c8564e155c67a6"))
"""