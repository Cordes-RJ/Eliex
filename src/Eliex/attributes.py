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
        self.extensions['paperpile'] = paperpileExt
        self.extensions['default'] = defaultExt
    def setNewSection(self, SectionName):
        self.currentSection = "[" + SectionName + "]"
    def readIn(self,String,**kwargs):
        Extension = "default"
        if "extension" in kwargs.keys():
            Extension = kwargs["extension"]
        self.read_string(self.currentSection+"\n" + self.extensions[Extension](String))
    # toString writes all attributes to an ini string which can be written to a .md
    def toString(self):
        string = ""
        for section in self.keys():
            for attribute in self[section].keys():
                string += (  attribute + " = " + str(self[section][attribute]) + "\n")
        return string

# default extension simply returns 
def defaultExt(s):
    return s

# paperpileExt is an extension meant to prep a paperpile string
def paperpileExt(s):
    ind1 = s.find('\n')
    ind2 = s.rfind('\n')
    #return s[ind1+1:ind2]
    x = s[ind1+1:ind2]
    ind1 = x.find('\n')
    ind2 = x.rfind('\n')
    return x[ind1+1:ind2]
    
"""
# set new section test
a = AttributeManager()
a.readIn("x = 32")
a.setNewSection("Test")
a.readIn("z = 47")
a['Test']['z'] = 47

# simple test
a = AttributeManager()
a.readIn("x = 32")
a.readIn("b = 17")
x = a['DEFAULT']['b']
"""

"""
# paperpile test
a = AttributeManager()
a.readIn(input("please input: "), extension="paperpile")
print("\n\n\n\n")
print(a.toString())

"""

