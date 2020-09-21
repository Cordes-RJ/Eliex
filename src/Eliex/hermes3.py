# -*- coding: utf-8 -*-
import utilFile
import fileHandler
import attributes
import listener
import config
import os

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

# mainLoop runs a main prompt loop for file import and listener
        # returns used in lieu of while loop for readability and clarity of
        # exit conditions.
def mainLoop(C):
    F = listening(C['DEFAULT']['Repo']+"/import",int(C['DEFAULT']['ListenTick'])) # listen until file-found
    fh = fileHandler.FileHandler(C['DEFAULT']['Repo'],F) # instantiate filehandler
    B = foundAFilePrompt(fh) # ask user to confirm integration of file
    if B == False:
        return # exit loop
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
    
###################################
    # util

class Satchel:
    def __init__(self):
        self.PiF = ""
        self.Title = ""
        self.DocTitle = ""
        self.KWs = ""
        self.FileName = ""
    def Create(self):
        self.PiF = inputPiF()
        self.Title = inputTitle()
        self.DocTitle = inputDocTitle()
        self.KWs = inputKWs()
        return self,False
    def ProduceINIstring(self):
        INI = ""
        INI += backlinkBracketDoc(self.FileName) + "\n"
        INI += "Title = \"" + self.Title + "\"\n" 
        INI += "PiF = " + backlinkBracket(self.PiF) +"\n"
        INI += "Backlinks = "
        for i in self.KWs:
            INI += backlinkBracket(i)
        return INI
    
    

#################################
        #Input funcs
PiF = ""

def inputPiF():
    global PiF
    userinput = input("\nInput Project in Focus (PiF) callsign, hit ENTER to use last PiF used: ")
    if userinput == "":
        if PiF == "":
            PiF = "MISC"
    else:
        PiF = userinput
    return PiF

def inputTitle():
    userinput = input("\nPlease input title: ")
    return userinput, False

def inputDocTitle():
    userinput = input("\nPlease input doc title eg NameYear-ShortTitle: ")
    return userinput, False

def inputKWs():
    print("\nIf there are any backlinks you'd like to add, add here, hit ENTER with blank input to continue")
    KWs = []
    while True:
        userinput = input("\nInput backlink title or hit ENTER to complete: ")
        if userinput == "":
            return KWs, False
        else:
            if userinput == "Cancel":
                return [], True
            KWs.append(userinput)

###################################
    # util

def backlinkBracket(string):
    return "[[" + string + "]]"

def backlinkBracketDoc(string):
    return "![[" + string + "]]"
