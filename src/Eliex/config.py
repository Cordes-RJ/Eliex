# -*- coding: utf-8 -*-
import configparser

#ConfigManager reads in and stores parameters. Inherits from configparser class
class ConfigManager(configparser.ConfigParser):
    def __init__(self,filepath):
        self.filepath = filepath # store the filepath to enable later update
        configparser.ConfigParser.__init__(self) # call init from parent
        self.readIn() # build dictionary
    # ReadIn builds the configManager's dictionary
    def readIn(self):
        with open(self.filepath, "r") as configfile:
            self.read_file(configfile)
    # update returns a fresh config manager.
    def update(self):
        return ConfigManager(self.filepath) # return copy
            
"""
example usage
config.ini
[DEFAULT]
ListenTick = 5
----------------
x = ConfigManager('config.ini')
print(x['DEFAULT']['ListenTick'])  out: 5
"""
