# -*- coding: utf-8 -*-

import hashlib

def getMD5(filepath):
    with open(filepath, 'rb') as file:
        data = file.read()
    return hashlib.md5(data).hexdigest()
    
"""
x = getMD5('config.ini') out: de88ec9491a8b87697751db5cc5b2fd1
"""