# -*- coding: utf-8 -*-

import utilFile
import fileHandler
import attributes
import listener
import config
import os
import hermes2

#fh = fileHandler.FileHandler("testfolder","testfolder/import/test.txt")

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
        return True

# inputCallsign handles user input of a callsign for the file
        # will loop in case of illegal callsign.
def inputCallsign(fh):
    while True:
        print("\nPlease input a callsign, with no spaces or '-' marks, between 3 and 24 characters.")
        b = fh.addCallsign(input("input Callsign: "))
        if b:
            print("Thanks! Callsign accepted!")
            return
        else:
            print("Callsign illegal. Try again...")

# attributeInputHelp notifies user of potential commands and legal action
def attributeInputHelp():
    print("Use format: attributeName = attributeValue!")
    print("Use keyword: extension, to call an extension for input!")
    print("Use keyword: commit, to finish!")

# committingResponse notifies user of completion of task
def committingResponse():
    print("committing attributes to be saved...")

# inputAttributeWithExtension sets extension and then asks for input
def inputAttributeWithExtension(aManager,ext):
    if ext not in aManager.extensions.keys():
        print("extension," + ext +", not found.")
        return
    while True:
        try:
            print("Using extension: " + ext + "...")
            userinput = input("Please input compatible string:")
            aManager.readIn(userinput, extension = ext)
            return
        except:
            print("failed to parse string.")
            if input("try again? y/n: ") != "y":
                return

# handles input of default attribute         
def inputAttributeWithDefaultExtension(aManager, userinput):
    try:
        aManager.readIn(userinput)
    except:
        print("failed to parse string.")
        return

     
"""
# v001
# inputAttributePrompt handles the looping insertion of attributes
def inputAttributePrompt(aManager):
    print("\nWe can now add attributes...")
    while True:
        userinput = input("\nInput Basic Attribute: ")
        if userinput == "extension": # enters subloop for using extension
            inputAttributeWithExtension(aManager,input("Input Extension: "))
        elif userinput == "help": # calls help print
            attributeInputHelp()
        elif userinput == "cancel":
            if input("are you sure you want to cancel integration? y/n:") == "y":
                print("canceling...")
                return False
        elif userinput == "commit": # commit is the exit condition for loop
            committingResponse()
            return True
        else: # use default extension
            inputAttributeWithDefaultExtension(aManager,userinput)
"""
def inputAttributePrompt():
    return hermes2.Satchel().Create()

# atomicImport prompts filehandler to import files with atomicity       
def atomicImport(fh,aManager):
    print("importing files...")
    try:
        print("creating hash file...")
        fh.addToHashLib()
    except:
        print("failed to create hash, aborting...")
        fh.moveToFailedImport()
        return
    try:
        print("creating callsign file...")
        fh.addToCSLib()
    except:
        print("failed to create callsign file, aborting...")
        fh.moveToFailedImport()
        return
    try:
        print("creating md reference file...")
        fh.addReferenceMD(aManager.toString())
    except:
        print("failed to create reference file, aborting...")
        #print("aManagerString for reference>") # testing
        #print(aManager.toString())
        #print("------------------------------\n\n") # testing
        utilFile.delFile(fh.makeHashPath()) # remove hash file
        fh.moveToFailedImport()
        return
    try:
        print("creating doc literal...")
        fh.addToDocLib()
    except:
        print("failed to create doc file, aborting...")
        utilFile.delFile(fh.makeHashPath()) # remove hash file
        utilFile.delFile(fh.makeMdPath()) # remove md file
        fh.moveToFailedImport()
        return
    print(fh.callsign + " imported successfully!")
    return

def pushDocLinkBack(fh):
    doclink = os.path.abspath(fh.makeDocPath())
    print("Doc Link for Reference:\n" + doclink +"\n")
        

# mainLoop runs a main prompt loop for file import and listener
        # returns used in lieu of while loop for readability and clarity of
        # exit conditions.
def mainLoop(C):
    F = listening(C['DEFAULT']['Repo']+"/import",int(C['DEFAULT']['ListenTick'])) # listen until file-found
    fh = fileHandler.FileHandler(C['DEFAULT']['Repo'],F) # instantiate filehandler
    B = foundAFilePrompt(fh) # ask user to confirm integration of file
    if B == False:
        return # exit loop
    B = checkingForDuplicate(fh)
    if B == False:
        return # exit loop
    ##inputCallsign(fh) Call sign will have to be taken afterward
    aManager = attributes.AttributeManager()
    satchel,cancel = inputAttributePrompt()
    if cancel:
        print("Canceling Integration...")
        print("Moving to Failed Import")
        fh.moveToFailedImport()
    else: 
        fh.setCallsign(satchel.Callsign)
        aManager.readIn(satchel.ProduceINIstring())
        #B = inputAttributePrompt(aManager) This has to change
        #if B == False:
        #    return # exit loop
        atomicImport(fh,aManager)
        pushDocLinkBack(fh)
        print("-----------------------------------\n")
    
    
    # for testing v
    # print("\n\n\n\n\n----------------------------------")
    # print(aManager.toString())
    
    
"""
    
C = loadingConfigs()
for i in range(3):
    mainLoop(C)

"""


"""
x = foundAFilePrompt("C:/Users/xyz/Documents/Code/Eliex/src/Eliex/testfolder/import/test.txt")
"""
"""
fh = fileHandler.FileHandler("testfolder","testfolder/import/test.txt")
x= pleaseInputaCallsign(fh)
print("test: " + fh.callsign)
"""

    
    
