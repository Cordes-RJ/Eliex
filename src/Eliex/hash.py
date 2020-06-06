# -*- coding: utf-8 -*-

import hashlib

# getMD5 returns an MD5 hash of a file, will return "" on error.
def getMD5(filepath):
    with open(filepath, 'rb') as file:
        data = file.read()
    print("Unable to read: " + filepath)
    return hashlib.md5(data).hexdigest()
    
"""
x = getMD5('config.ini') out: de88ec9491a8b87697751db5cc5b2fd1
"""

