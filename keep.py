#! /usr/bin/env python3
# coding: utf-8

import os
import logging as lg
import colors as clr
import random as rd
import pickle
import hashlib as hl
import colorsLog as clg
import re
import ast

lg.basicConfig(level=lg.DEBUG)

DEFAULT_ALPHA = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789éèêàçùôîëï&\"\'.,;?/:!()-_=#{}[]\^@°+%*<>"
DEFAULT_ALPHA_HASH = "abcdefghijklmnopqrstuvwxyz0123456789"
DEFAULT_CARAC = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789àáâæçèéêëìíîïñòóôùúûüýÿÀÁÂÆÇÈÉÊËÌÍÎÏÑÒÓÔÙÚÛÜÝ.,;?/:!&\"\'()-_=~#{}[]|\^@°+£%*<>$"

def _loadExtension():
    _extensions = {}
    try :
        with open("settings/extensions.txt", "r") as f:
            for i in f.readlines():
                t = re.sub(r"^(?P<n>.*) : \"(?P<e>\.[\w]*)\"$", "\g<n>;\g<e>", i.replace("\n", ''))
                n, e = t.split(";")
                _extensions[n] = e
    except FileNotFoundError :
        clg.critical("Error in loading of extensions's files. \nFile not found.\nProgram is stoping...\n")
    return _extensions

def __hashText(text):
    return hl.sha1(text.encode()).hexdigest()

def importDictios(dictioName):
    if dictios.get(dictioName):
        return dictios.get(dictioName)
    dictio = {
        "alpha" : {},
        "alphaHash" : {},
        "carac" : {}
    }
    dictioNamePath = "dictionnaries/{}.dct".format(dictioName).lower()
    with open(dictioNamePath, "rb") as f:
        fp = pickle.Unpickler(f)
        dictio = fp.load()
    return dictio

def generateDictio(overWrite = True, saveReadable = False, dictioName = "default", alpha = DEFAULT_ALPHA, carac = DEFAULT_CARAC, alphaHash = DEFAULT_ALPHA_HASH):
    dictio = {
        "alpha" : {
            "encrypt" : {},
            "decrypt" : {}
        },
        "alphaHash" : {
            "encrypt" : {},
            "decrypt" : {}
        },
        "carac" : {
            "encrypt" : {},
            "decrypt" : {}
        },
        "settings" : {
            "overWrite" : overWrite,
            "saveReadable" : saveReadable,
            "alpha" : alpha,
            "alphaHash" : alphaHash,
            "carac" : carac
        }
    }
    clg.debug(dictio.get("settings"))
    for i in range(len(alpha)):
        ((dictio.get("alpha")).get("encrypt"))[alpha[i]] = i
        ((dictio.get("alpha")).get("decrypt"))[i] = alpha[i]
    for i in range(len(alphaHash)):
        ((dictio.get("alphaHash")).get("encrypt"))[alphaHash[i]] = i
        ((dictio.get("alphaHash")).get("decrypt"))[i] = alphaHash[i]
    for i in range(len(carac)):
        tmp = rd.choice(carac)
        ((dictio.get("carac")).get("encrypt"))[tmp] = i
        ((dictio.get("carac")).get("decrypt"))[i] = tmp
        carac = carac.replace(tmp, '')
    dictioNamePath = "dictionnaries/{}."
    with open(dictioNamePath.format(dictioName).lower() + "dct", "wb") as f:
        fp = pickle.Pickler(f)
        fp.dump(dictio)
    if saveReadable:
        with open(dictioNamePath.format("readable_"+dictioName).lower() + "rdct", "w") as f:
            f.write("Readable dictionnaries of {} dictionnaries.\nAlpha's characters\n\tEncode characters : \n".format(dictioName))
            for i, j in dictio.get("alpha").get("encrypt").items():
                f.write("- {} > {} \n".format(i, j))
            f.write("\tDecode characters : \n")
            for i, j in dictio.get("alpha").get("decrypt").items():
                f.write("- {} > {} \n".format(i, j))
            f.write("Alpha hash's characters\n\tEncode characters : \n".format(dictioName))
            for i, j in dictio.get("alphaHash").get("encrypt").items():
                f.write("- {} > {} \n".format(i, j))
            f.write("\tDecode characters : \n")
            for i, j in dictio.get("alphaHash").get("decrypt").items():
                f.write("- {} > {} \n".format(i, j))
            f.write("Carac's characters\n\tEncode characters : \n".format(dictioName))
            for i, j in dictio.get("carac").get("encrypt").items():
                f.write("- {} > {} \n".format(i, j))
            f.write("\tDecode characters : \n")
            for i, j in dictio.get("carac").get("decrypt").items():
                f.write("- {} > {} \n".format(i, j))

    allDictio.append(dictioName)
    saveDictio()
    return False

def encrypt(communText, encryptText, dictioName):
    """if len(communText) < len(encryptText):
        try :
            raise Warning("Commun Text too short. \nIt must be longer than the text to encrypt.\n")
        except Warning as e:
            clr.yellow()
            lg.warning("Error : {}".format(e))
            clr.reset()
            return True, None"""
    try :
        dictio = importDictios(dictioName)
    except Warning as e :
        clg.critical("Dictionnaries not found.\n{}\nProgram is stoping...\n".format(e))
        return True, None
    hashCommunText = __hashText(communText)
    tmpHashCommunText = hashCommunText
    while len(tmpHashCommunText) < len(encryptText):
        tmpHashCommunText += hashCommunText
    hashCommunText = tmpHashCommunText
    del(tmpHashCommunText)
    j = 0
    out = ""
    for i in encryptText:
        out += ((dictio.get("carac")).get("decrypt")).get(((dictio.get("alpha")).get("encrypt")).get(i) + ((dictio.get("alphaHash")).get("encrypt")).get(hashCommunText[j]))
        j += 1
    return False, out

def decrypt(communText, encryptedText, dictioName):
    try :
        dictio = importDictios(dictioName)
    except DictioNotFoundError as e :
        clr.yellow()
        lg.warning("Dictionnaries not found.\n{}".format(e))
        clr.reset()
        return True, None
    hashCommunText = __hashText(communText)
    tmpHashCommunText = hashCommunText
    while len(tmpHashCommunText) < len(encryptedText):
        tmpHashCommunText += hashCommunText
    hashCommunText = tmpHashCommunText
    j = 0
    out = ""
    for i in encryptedText:
        out += ((dictio.get("alpha")).get("decrypt")).get(((dictio.get("carac")).get("encrypt")).get(i) - ((dictio.get("alphaHash")).get("encrypt")).get(hashCommunText[j]))
        j += 1
    return False, out

def getDictio():
    with open("settings/dictios.txt") as f:
        text = f.readline()
    return ast.literal_eval(text)

def saveDictio():
    with open("settings/dictios.txt", "w") as f:
        f.write("{}".format(allDictio))

def removeDictio(dictioName):
    allDictio.remove(dictioName)
    clg.debug(allDictio)
    saveDictio()
    os.remove("dictionnaries/{}.dct".format(dictioName))
    try :
        os.remove("dictionnaries/readable_{}.rdct".format(dictioName))
    except FileNotFoundError :
        pass


dictios = {}
allDictio = getDictio()

def main():
    for i in allDictio:
        dictios[i] = importDictios(i)
    _extensions = _loadExtension
    generateDictio()
    t = encrypt("Bonjour", "Test", "default")[1]
    print("The encrypted text 'Test' encrypt with KEEP with 'Bonjour' in commun text is : ", t)
    #print(decrypt("Bonjour", t, "default")[1])
    t = encrypt("Bonjour", "Ceci est un test de chiffrage avec la méthode KEEP. Nous espérons tous que cela marchera.", "default")[1]
    print(t)
    print(decrypt("Bonjour", t, "default")[1])
    return False

if __name__ == "__main__":
    main()
    os.system("pause")
