# -*- coding: utf-8 -*-

import utilFile

class FileHandler:
    def __init__(self):
        self.callsign = ""
        self.hash = ""
    # addCallsign returns true if set to standard and false if it fails
    # character limit of callsign (24chars)
    def addCallsign(self,string):
        if len(string) >= 24:
            return False
        self.callsign = string + ((24 - len(string))*"_")
        return True
    # checkHash saves the hash to the manager's cache, and then checks for
    # the hash's existence in the hashLib to see if the hash is a duplicate.
    # if the hash is a duplicate, returns True, else returns False.
    def checkHash(self,repoPath,Hash):
        self.hash = Hash
        return utilFile.checkForFile(repoPath+Hash)
    
    
"""
f = FileHandler()
x = f.addCallsign("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
x = f.addCallsign("test")
y = f.callsign
"""

"""
f = FileHandler()
x = f.checkHash("testfolder/hashLib/","de88ec9491a8b87697751db5cc5xafd1")
"""
