# -*- coding: utf-8 -*-

import utilFile
import fileHandler

def foundAFilePrompt(filepath):
    print("Eliex found a file: " + utilFile.getFileName(filepath)
    + "\nShould we integrate it?")
    if input("y/n: ") == "y":
        return True
    print("No Problem! Moving file to failedImport!")
    return False

def foundDuplicate(filepath, Hash):
    print("We already have this file!")
    print("Search in obsidian for the hash: " + Hash)
    
def pleaseInputaCallsign(fh):
    while True:
        print("Please input a callsign, with no spaces or '-' marks, between 3 and 24 characters.")
        b = fh.addCallsign(input("input Callsign: "))
        if b:
            print("Thanks! Callsign accepted!")
            return
        else:
            print("Callsign illegal. Try again...")

"""
x = foundAFilePrompt("C:/Users/xyz/Documents/Code/Eliex/src/Eliex/testfolder/import/test.txt")
"""
"""
fh = fileHandler.FileHandler("testfolder","testfolder/import/test.txt")
x= pleaseInputaCallsign(fh)
print("test: " + fh.callsign)
"""

    
    
