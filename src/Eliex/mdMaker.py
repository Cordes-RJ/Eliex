# -*- coding: utf-8 -*-

import utilTime
import os

# mdStringMake creates a v001 ved-header, adds essential metadata, and tacks
# additional found attributes to the bottom
def mdStringMake(string, fileName):
    # for readability, split into multiple lines
    ved = ".vedhead.lit.v003\n"
    ved += "\n\n\n\n\n\n\n\n\n\n.ved\n"
    ved += ("dateadded = " + str(utilTime.getDate()) + "\n")
    ved += "timestamp = " +str(utilTime.getTimeStamp()) + "\n"
    ved += "literalReference = " + os.path.abspath(fileName) + "\n"
    #print("testing: Made it past os.path.abspath") # testing
    ved += string
    return ved

"""
x = mdStringMake("testing = s", "callsign-THISISSOMERANDOMHASHSTRING")
"""