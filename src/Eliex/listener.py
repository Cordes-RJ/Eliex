# -*- coding: utf-8 -*-

import os
from time import sleep

# Listener listens for changes in a folder
class Listener:
    def __init__(self, folder, tick):
        self.folder = folder # directory to be listened to
        self.tick = tick # seconds between checks on directory
    def getPaths(self): # returns all paths in a directory
        paths = []
        for path in os.listdir(self.folder):
            fullpath = os.path.join(self.folder,path)
            if os.path.isfile(fullpath):
                paths.append(fullpath)
        return paths
    def SetTick(self, tick): # update function for tick
        self.tick = tick
    def Listen(self):
        while True:
            #print("tick...") # For testing
            paths = self.getPaths()
            if len(paths) != 0:
                return paths[0]
            sleep(self.tick)
            
"""
L = Listener("testfolder",5)
x = L.Listen()
"""