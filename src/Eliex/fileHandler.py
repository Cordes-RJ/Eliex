# -*- coding: utf-8 -*-

import utilFile
import utilHash
import mdMaker
import os

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
        if "-" in string:
            return False
        self.callsign = string
        return True
    #checkCallSign checks the csLib to see if the callSign is a duplicate
    def checkCallSign(self):
        return utilFile.checkForFile(self.makeCallSignPath())
    # checkHash checks in the hashLib to see if the hash is a duplicate.
    # if the hash is a duplicate, returns True, else returns False.
    def checkHash(self):
        return utilFile.checkForFile(self.makeHashPath())
    # addToHashLib adds a pointer-file to hash library
    def addToHashLib(self):
        utilFile.makeFile(self.makeHashPath(),"")
    # addToDocLib moves file to docLib with new name (callsign + hash)
    def addToDocLib(self):
        utilFile.editFilePath(self.filepath,self.makeDocPath())
    def addReferenceMD(self,string):
        #fp = self.repoPath+"/docLib/"+self.callsign+"-"+self.hash
        mdString = mdMaker.mdStringMake(string, self.makeDocPath())
        #utilFile.makeFile(self.repoPath+"/mdLib/"+self.callsign+"-"+self.hash, mdString)
        utilFile.makeFile(self.makeMdPath(), mdString)
    def moveToFailedImport(self):
        utilFile.editFilePath(self.filepath,self.repoPath+"/failedImport/"+utilFile.getFileName(self.filepath))
    def makeDocPath(self):
        return self.repoPath+"/docLib/"+self.callsign+"-"+self.hash+utilFile.getExt(self.filepath)
    def makeMdPath(self):
        return self.repoPath+"/mdLib/"+self.callsign + ".md"
    def makeHashPath(self):
        return self.repoPath+"/hashLib/"+self.hash
    def makeCallSignPath(self):
        return self.repoPath+"/csLib/"+self.hash
          
#%%


#%%


"""
f = FileHandler("testfolder","testfolder/testy2.txt")
f.moveToFailedImport()
"""

"""
f = FileHandler()
x = f.addCallsign("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
x = f.addCallsign("test")
y = f.callsign


f = FileHandler("testfolder","testfolder/test2.txt")
x = f.hash
x = f.checkHash()
f.addToHashLib()
x = f.addCallsign("TEST_Item")
f.addToDocLib()
f.addReferenceMD("testing")
"""