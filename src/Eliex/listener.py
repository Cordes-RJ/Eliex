# -*- coding: utf-8 -*-

import os

# Listener listens for changes in a folder
class Listener:
    def __init__(self, folder, configmngr):
        self.folder = folder
        self.configmngr = configmngr
    def getPaths(self):
        paths = []
        for path in os.listdir(self.folder):
            fullpath = os.path.join(self.folder,path)
            if os.path.isfile(fullpath):
                paths.append(fullpath)
        return paths
    def Listen(self):
        while True:
            time.sleep(self.configmngr['DEFAULT']['ListenTick'])
            
    

"""
import config
c = config.ConfigManager('config.ini')
L = Listener("testfolder", c)
x = L.getPaths()
"""