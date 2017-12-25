#! /usr/bin/env/ python
# coding: utf-8

import os
import __var as _vr

try :
    os.mkdir("dictionnaries")
except FileExistsError :
    pass
try :
    os.mkdir("settings")
except FileExistsError :
    pass

with open("settings/dictios.txt", "w") as f:
    f.write("[]")
with open("settings/extensions.txt", "w") as f:
    f.write('dictionnariesFile : ".dictio"\nalphaFile : ".alpha"\nalphaHashFile : ".alphaHash"\ncaracFile : ".carac"\nkeysFile : ".keys"\nencryptS_File : ".keeps"\nencryptA_S_File : ".keepas"\n')

import keep

keep.generateDictio(saveReadable = True)
