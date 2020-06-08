# -*- coding: utf-8 -*-

class FileHandler:
    def __init__(self):
        self.callsign = ""
    # addCallsign returns true if set to standard and false if it fails
    # character limit of callsign (24chars)
    def addCallsign(self,string):
        if len(string) >= 24:
            return False
        self.callsign = string + ((24 - len(string))*"_")
        return True
    
    
"""
f = FileHandler()
x = f.addCallsign("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
x = f.addCallsign("test")
y = f.callsign
"""
