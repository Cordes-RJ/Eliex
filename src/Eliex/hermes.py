# -*- coding: utf-8 -*-

import utilFile
import fileHandler
import attributes
import listener
import config

#fh = fileHandler.FileHandler("testfolder","testfolder/import/test.txt")

# loadingConfigs loads configs and returns a config manager to loop
def loadingConfigs():
    print("Loading configuration...")
    return config.ConfigManager("config.ini")

# listening notifies user of status and listens for new files
def listening(folder,tick):
    print("Opening listening post...")
    L = listener.Listener(folder, tick)
    print("Listening...")
    return L.Listen()

# foundAFilePrompt asks a user to confirm integration of a file
def foundAFilePrompt(fh):
    print("Eliex found a file: " + utilFile.getFileName(fh.filePath)
    + "\nShould we integrate it?")
    if input("y/n: ") == "y":
        return True
    moveToFailedImport(fh)
    return False

# moveToFailedImport moves a canceled or failed file to another folder
def moveToFailedImport(fh):
    print("Moving file to failedImport!")
    fh.moveToFailedImport()

# checkingForDuplicate checks for a duplicate hash
    # returns True if no duplicate found, else false.
def checkingForDuplicate(fh):
    #fh = fileHandler.FileHandler("testfolder","testfolder/import/test.txt")
    b = fh.checkHash()
    if b:
        print("We already have this file!")
        print("Search in obsidian for the hash: " +fh.hash)
        moveToFailedImport(fh)
        return False
    else:
        True


#%%
# mainLoop runs a main prompt loop for file import and listener
        # returns used in lieu of while loop for readability and clarity of
        # exit conditions.
def mainLoop(C):
    F = listening(C['DEFAULT']['Repo']+"/import",int(C['DEFAULT']['ListenTick'])) # listen until file-found
    fh = fileHandler.FileHandler(C['DEFAULT']['Repo'],F) # instantiate filehandler
    B = foundAFilePrompt() # ask user to confirm integration of file
    if B == False:
        return # exit loop
    B = checkingForDuplicate(fh)
    if B == False:
        return # exit loop
    
    
    
    
C = loadingConfigs()
mainLoop(C)

 
#%%

    


def checkingForDuplicate(fh):
    #fh = fileHandler.FileHandler("testfolder","testfolder/import/test.txt")
    b = fh.checkHash()
    if b:
        print("We already have this file!")
        print("Search in obsidian for the hash: " +fh.hash)
        moveToFailedImport(fh)
        return False
    else:
        True

def pleaseInputaCallsign(fh):
    while True:
        print("Please input a callsign, with no spaces or '-' marks, between 3 and 24 characters.")
        b = fh.addCallsign(input("input Callsign: "))
        if b:
            print("Thanks! Callsign accepted!")
            return
        else:
            print("Callsign illegal. Try again...")


##
def pleaseInputAttributes():
    a = attributes.AttributeManager()

"""
x = foundAFilePrompt("C:/Users/xyz/Documents/Code/Eliex/src/Eliex/testfolder/import/test.txt")
"""
"""
fh = fileHandler.FileHandler("testfolder","testfolder/import/test.txt")
x= pleaseInputaCallsign(fh)
print("test: " + fh.callsign)
"""

    
    
