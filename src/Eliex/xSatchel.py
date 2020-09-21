# -*- coding: utf-8 -*-

class Satchel:
    def __init__(self):
        self.PiF = ""
        self.Title = ""
        self.DocTitle = ""
        self.KWs = ""
        self.FileName = ""
        self.Hash = ""
    def Create(self):
        self.PiF, Cancel = inputPiF()
        if Cancel:
            return self,True
        self.Title, Cancel = inputTitle()
        if Cancel:
            return self,True
        self.DocTitle, Cancel = inputDocTitle()
        if Cancel:
            return self,True
        self.KWs, Cancel = inputKWs()
        if Cancel:
            return self,True
        return self,False
    def GiveFileNameandHash(self, FileName,Hash):
        self.FileName = FileName
        self.Hash = Hash
    def ProduceINIstring(self):
        INI = ""
        INI += backlinkBracketDoc(self.FileName) + "\n"
        INI += "Hash = " + self.Hash + "\n"
        INI += "Title = \"" + self.Title + "\"\n" 
        INI += "PiF = " + backlinkBracket("PIF - " + self.PiF) +"\n"
        INI += "Backlinks = "
        for i in self.KWs:
            INI += backlinkBracket(i) + ", "
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
    elif userinput == "Cancel":
        return userinput, True
    else:
        PiF = userinput
    return PiF, False

def inputTitle():
    userinput = input("\nPlease input title: ")
    if userinput == "Cancel":
        return "", True
    return userinput, False

def inputDocTitle():
    userinput = input("\nPlease input doc title eg NameYear-ShortTitle: ")
    if userinput == "Cancel":
        return "", True
    return userinput, False

def inputKWs():
    print("\nIf there are any backlinks you'd like to add, add here, hit ENTER with blank input to continue")
    KWs = []
    while True:
        userinput = input("\nInput backlink title or hit ENTER to complete: ")
        if userinput == "":
            return KWs, False
        elif userinput == "Cancel":
            return [], True
        else:
            KWs.append(userinput)

###################################
    # util

def backlinkBracket(string):
    return "[[" + string + "]]"

def backlinkBracketDoc(string):
    return "![[" + string + "]]"

