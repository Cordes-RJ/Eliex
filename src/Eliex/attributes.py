# -*- coding: utf-8 -*-

import configparser

class AttributeManager(configparser.ConfigParser):
    def __init__(self):
        configparser.ConfigParser.__init__(self,allow_no_value=True)
        self.currentSection = "[DEFAULT]"
        self.extensions = {} # extension keywords to functions,
        # this enables the use of particular extensions to import attributes
        # from particular formats such as JSON or Paperpile which cannot be
        # read using the attribute manager's default reader which is intended
        # to read ini files.
        #self.extensions['paperpile'] = ...
    def setNewSection(self, SectionName):
        self.currentSection = "[" + SectionName + "]"
    def readIn(self,String):
        self.read_string(self.currentSection+"\n" + String)
    
"""
a = AttributeManager()
a.readIn("x = 32")
a.setNewSection("Test")
a.readIn("z = 47")
"""
"""
a = AttributeManager()
a.readIn(input("please input: "))
x = [a]
"""