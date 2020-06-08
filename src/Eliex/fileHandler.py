# -*- coding: utf-8 -*-

import utilFile
import utilHash

class FileHandler:
    def __init__(self, repoPath, filepath):
        self.callsign = ""
        self.hash = utilHash.getMD5(filepath)
        self.repoPath = repoPath
        self.filepath = filepath
    # addCallsign returns true if set to standard and false if it fails
    # character limit of callsign (24chars)
    def addCallsign(self,string):
        if len(string) >= 24:
            return False
        if " " in string:
            return False
        self.callsign = string + ((24 - len(string))*"_")
        return True
    # checkHash checks in the hashLib to see if the hash is a duplicate.
    # if the hash is a duplicate, returns True, else returns False.
    def checkHash(self):
        return utilFile.checkForFile(self.repoPath+"/hashLib/"+self.hash)
    def addToHashLib(self):
        utilFile.makeFile(self.repoPath+"/hashLib/"+self.hash,"")
    def addToDocLib(self):
        utilFile.editFilePath(self.filepath,self.repoPath+"/docLib/"+self.callsign+"-"+self.hash)
    
"""
f = FileHandler()
x = f.addCallsign("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
x = f.addCallsign("test")
y = f.callsign
"""

#%%
f = FileHandler("testfolder","testfolder/test.txt")
x = f.hash
#%%
x = f.checkHash()
#%%
f.addToHashLib()
x = f.addCallsign("TEST Item")
#%%
f.addToDocLib()
