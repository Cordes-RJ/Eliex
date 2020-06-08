# -*- coding: utf-8 -*-

import utilTime
import os

# mdStringMake creates a v001 ved-header, adds essential metadata, and tacks
# additional found attributes to the bottom
def mdStringMake(string, fileName):
    # for readability, split into multiple lines
    ved = ".vedhead.lit.v001\n"
    ved += ("dateadded = " + str(utilTime.getDate()) + "\n")
    ved += "timestamp = " +str(utilTime.getTimeStamp()) + "\n"
    ved += "literalReference = " + os.path.abspath(fileName) + "\n"
    ved += string
    return ved

"""
x = mdStringMake("testing = s", "callsign-THISISSOMERANDOMHASHSTRING")
"""