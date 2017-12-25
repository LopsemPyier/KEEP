#! /usr/bin/env python3
# coding: utf-8

import keep
import __var as _vr
import colorsLog as clg

window = None
clg.debugLevel()

def generate():
    overWrite = window.overwrite.get()
    saveReadable = window.saveReadable.get()
    dictioName = window.nameDic.get()
    carac = _vr.carac.get(window.choiceAlpha.get())
    keep.generateDictio(overWrite, saveReadable, dictioName, carac.get("DEFAULT_ALPHA"), carac.get("DEFAULT_CARAC"), carac.get("DEFAULT_ALPHA_HASH"))
    window.dictioToImport.insert("end", dictioName)

def importDictios():
    pass

def encrypt():
    res = keep.encrypt(window.eCommunText.get(), window.eEncryptText.get(), window.eDictioToUse.get(window.eDictioToUse.curselection()))[1]
    window.encryptedTextVal.set(res)
    return res

def saveInFile():
    filePath = window._fileToSave()
    with open(filePath, "w") as f:
        f.write(encrypt())

def decrypt():
    res = keep.decrypt(window.dCommunText.get(), window.dEncryptText.get(), window.dDictioToUse.get(window.dDictioToUse.curselection()))[1]
    window.decryptedTextVal.set(res)
    return res
