# -*- coding: utf-8 -*-

# Get Extension of file from filepath string 
def getExt(filepath):
    i = filepath.rindex(".")
    return filepath[i:len(filepath)]
    


"""
print(getExt("testfolder\test.txt"))
"""