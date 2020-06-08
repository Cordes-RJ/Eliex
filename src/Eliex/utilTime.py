# -*- coding: utf-8 -*-

import datetime

# Gets date and time in string format
def getDate():
    return datetime.datetime.today().strftime ('%d-%b-%Y %H:%M:%S')

# Gets timestamp in float format
def getTimeStamp():
    return datetime.datetime.timestamp(datetime.datetime.now())

"""
x = getTimeStamp()
y = getDate()
"""
