# -*- coding: utf-8 -*-
import utilFile
import utilHash
import fileHandler
import attributes
import listener
import config
import os
import xSatchel



# loadingConfigs loads configs and returns a config manager to loop
def loadingConfigs():
    print("Loading configuration...")
    return config.ConfigManager("C:/Users/xyz/Documents/Code/Eliex/src/Eliex/config.ini")

# listening notifies user of status and listens for new files
def listening(folder,tick):
    print("Opening listening post...")
    L = listener.Listener(folder, tick)
    print("Listening...")
    return L.Listen()

# foundAFilePrompt asks a user to confirm integration of a file
def foundAFilePrompt(fh):
    print("\nEliex found a file: " + utilFile.getFileName(fh.filepath)
    + "\nShould we integrate it?")
    if input("y/n: ") == "y":
        return True
    moveToFailedImport(fh)
    return False

# moveToFailedImport moves a canceled or failed file to another folder
def moveToFailedImport(fh):
    print("Moving file to failedImport!")
    try :
        fh.moveToFailedImport()
    except:
        print("Warning: Failed to move file!")
        
def checkingForDuplicate(fh):
    #fh = fileHandler.FileHandler("testfolder","testfolder/import/test.txt")
    b = fh.checkHash()
    if b:
        print("We already have this file!")
        print("Search in obsidian for the hash: " +fh.hash)
        moveToFailedImport(fh)
        return False
    else:
        return True
        
def mainLoop(C):
    F = listening(C['DEFAULT']['Repo']+"/import",int(C['DEFAULT']['ListenTick'])) # listen until file-found
    fh = fileHandler.FileHandler(C['DEFAULT']['Repo'],F) # instantiate filehandler
    B = foundAFilePrompt(fh) # ask user to confirm integration of file
    if B == False:
        return # exit loop
    B = checkingForDuplicate(fh)
    if B == False:
        return # exit loop
    satchel,cancel = xSatchel.Satchel().Create()
    if cancel:
        print("Canceling Integration...")
        print("Moving to Failed Import")
        fh.moveToFailedImport()
    satchel.Hash = fh.hash
    satchel.FileName = "docLib/" + satchel.DocTitle + utilFile.getExt(F)
    fh.callsign = satchel.DocTitle
    fh.addReferenceMD(satchel.ProduceINIstring())
    fh.addToDocLib()
    fh.addToHashLib()
    print("Done...\n--------------------------------------------\n")

"""
C = loadingConfigs()
mainLoop(C)
"""