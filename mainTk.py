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
import tkinter as tk
import colorsLog as clg
import __var as _vr
import __keepTk as _kTk
import tkinter.filedialog as tkF

import keep

class Display():
    def __init__(self, win):
        self.dictio = keep.getDictio()
        clg.debug(self.dictio)

        self.window = win
        self.menu = tk.Frame(self.window)
        self.keeps = tk.Frame(self.menu).pack()
        self.keepas = tk.Frame(self.menu).pack()
        self.generate = tk.Frame(self.window).pack()
        self.imports = tk.Frame(self.window).pack()
        self.encryptFrame = tk.Frame(self.window).pack()
        self.decryptFrame = tk.Frame(self.window).pack()

        self.title = tk.Label(self.window, text = "KEEP S or AS.\nKey Encryptor Encodage Processus.\nSymetrical or Asymetrical and Symetrical.")
        self.quitButton = tk.Button(self.window, text = "Quit", command = self.window.quit)

        self.titleKeeps = tk.Label(self.keeps, text = "\nKEEP Symetrical : ")
        self.encryptKeepsButton = tk.Button(self.keeps, text = "Encrypt", command = self.encryptS)
        self.decryptKeepsButton = tk.Button(self.keeps, text = "Decrypt", command = self.decryptS)
        self.generateButton = tk.Button(self.keeps, text = "Generate dictionnaies", command = self.generateDic)
        self.importButton = tk.Button(self.keeps, text = "Import dictionnaries", command = self.importDic)
        self.backButton = tk.Button(self.window, text = "Back to menu", command = self.back)

        self.eCommunText = tk.StringVar()
        self.eCommunTextLab = tk.Label(self.encryptFrame, text = "Enter the commun text : ")
        self.eCommunTextEnt = tk.Entry(self.encryptFrame, textvariable = self.eCommunText, width = 40)
        self.eEncryptText = tk.StringVar()
        self.eEncryptTextLab = tk.Label(self.encryptFrame, text = "Enter the text to encrypt : ")
        self.eEncryptTextEnt = tk.Entry(self.encryptFrame, textvariable = self.eEncryptText, width = 40)
        self.eDictioLab = tk.LabelFrame(self.encryptFrame, text = "Choose dictionnaries to use : ")
        self.eDictioToUse = tk.Listbox(self.eDictioLab)
        for i in self.dictio:
            self.eDictioToUse.insert("end", i)
        self.eEncryptTextButton = tk.Button(self.encryptFrame, text = "Encrypt", command = _kTk.encrypt)
        self.saveInFile = tk.Button(self.encryptFrame, text = "Save the encrypted text in a file", command = _kTk.saveInFile)
        self.encryptedTextVal = tk.StringVar()
        self.encryptedTextL = tk.Label(self.encryptFrame, text = "The encrypted text : ")
        self.encryptedTextLab = tk.Entry(self.encryptFrame, textvariable = self.encryptedTextVal)

        self.dCommunText = tk.StringVar()
        self.dCommunTextLab = tk.Label(self.decryptFrame, text = "Enter the commun text : ")
        self.dCommunTextEnt = tk.Entry(self.decryptFrame, textvariable = self.dCommunText, width = 40)
        self.dEncryptText = tk.StringVar()
        self.dEncryptTextLab = tk.Label(self.decryptFrame, text = "Enter the text to decrypt : ")
        self.dEncryptTextEnt = tk.Entry(self.decryptFrame, textvariable = self.dEncryptText, width = 40)
        self.dDictioLab = tk.LabelFrame(self.decryptFrame, text = "Choose dictionnaries to use : ")
        self.dDictioToUse = tk.Listbox(self.dDictioLab)
        for i in self.dictio:
            self.dDictioToUse.insert("end", i)
        self.decryptTextButton = tk.Button(self.decryptFrame, text = "Decrypt", command = _kTk.decrypt)
        self.decryptedTextVal = tk.StringVar()
        self.decryptedTextL = tk.Label(self.decryptFrame, text = "The decrypted text : ")
        self.decryptedTextLab = tk.Entry(self.decryptFrame, textvariable = self.decryptedTextVal)

        self.caracFrame = tk.LabelFrame(self.generate, text = "Choose a characters' type.")
        self.choiceAlpha = tk.StringVar()
        self.alphanumChoice = tk.Radiobutton(self.caracFrame, text="Alpha-numérique", variable = self.choiceAlpha, value = "ALPHANUM")
        self.defaultChoice = tk.Radiobutton(self.caracFrame, text="Default choice", variable = self.choiceAlpha, value = "DEFAULT")
        self.validButton = tk.Button(self.generate, text="Generate", command = _kTk.generate)
        self.nameDicLab = tk.Label(self.generate, text = "Enter the name of the dictionnaries : ")
        self.nameDic = tk.StringVar()
        self.nameDicText = tk.Entry(self.generate, textvariable = self.nameDic, width = 30)
        self.overwrite = tk.IntVar()
        self.overwriteCase = tk.Checkbutton(self.generate, text = "Overwrite if dictionnaries' name already taken.", variable = self.overwrite)
        self.saveReadable = tk.IntVar()
        self.saveReadableCase = tk.Checkbutton(self.generate, text = "Save dictionnaries also in readable files.", variable = self.saveReadable)

        self.dictiosFrame = tk.LabelFrame(self.imports, text = "Dictionnaries already imported : ")
        self.dictioToImport = tk.Listbox(self.dictiosFrame)
        self.importDictioButton = tk.Button(self.imports, text = "Choose other dictionnaries", command=self._import)
        self.deleteDictioButton = tk.Button(self.imports, text = "Delete dictionnaries", command=self.delDictio)
        self.updateDictioButton = tk.Button(self.imports, text = "Update dictionnaries", command=self.updateDictio)
        for i in self.dictio:
            self.dictioToImport.insert("end", i)
            keep.dictios[i] = keep.importDictios(i)
            clg.debug("Loading {} dictionnaries.\n".format(i))

        self.title.pack(side = "top")
        self.quitButton.pack(side = "top")

        self.titleKeeps.pack(side = "top")
        self.encryptKeepsButton.pack(side = "top")
        self.decryptKeepsButton.pack(side = "top")
        self.generateButton.pack(side = "top")
        self.importButton.pack(side = "top")

        self.menu.pack()


    def encryptS(self):
        self.encryptKeepsButton.pack_forget()
        self.decryptKeepsButton.pack_forget()
        self.generateButton.pack_forget()
        self.importButton.pack_forget()
        self.menu.pack_forget()
        self.backButton.pack(side = "left")
        self.eCommunTextLab.pack()
        self.eCommunTextEnt.pack()
        self.eEncryptTextLab.pack()
        self.eEncryptTextEnt.pack()
        self.eDictioLab.pack()
        self.eDictioToUse.pack()
        self.eEncryptTextButton.pack()
        self.saveInFile.pack()
        self.eDictioToUse.selection_set(keep.allDictio.index("default"))
        self.encryptedTextL.pack()
        self.encryptedTextLab.pack()

    def decryptS(self):
        self.encryptKeepsButton.pack_forget()
        self.decryptKeepsButton.pack_forget()
        self.generateButton.pack_forget()
        self.importButton.pack_forget()
        self.menu.pack_forget()
        self.backButton.pack(side = "left")
        self.dCommunTextLab.pack()
        self.dCommunTextEnt.pack()
        self.dEncryptTextLab.pack()
        self.dEncryptTextEnt.pack()
        self.dDictioLab.pack()
        self.dDictioToUse.pack()
        self.dDictioToUse.selection_set(keep.allDictio.index("default"))
        self.decryptTextButton.pack()
        self.decryptedTextL.pack()
        self.decryptedTextLab.pack()

    def generateDic(self):
        self.encryptKeepsButton.pack_forget()
        self.decryptKeepsButton.pack_forget()
        self.generateButton.pack_forget()
        self.importButton.pack_forget()
        self.menu.pack_forget()
        self.choiceAlpha.set("DEFAULT")
        self.backButton.pack(side = "left")
        self.nameDicLab.pack()
        self.nameDicText.pack()
        self.defaultChoice.pack()
        self.alphanumChoice.pack()
        self.caracFrame.pack()
        self.overwriteCase.pack()
        self.saveReadableCase.pack()
        self.validButton.pack()


    def importDic(self):
        self.encryptKeepsButton.pack_forget()
        self.decryptKeepsButton.pack_forget()
        self.generateButton.pack_forget()
        self.importButton.pack_forget()
        self.menu.pack_forget()
        self.updateDictioButton.pack()
        self.deleteDictioButton.pack()
        self.backButton.pack(side = "left")
        self.dictiosFrame.pack()
        self.dictioToImport.pack()
        self.importDictioButton.pack()

    def back(self):
        self.menu.pack()
        self.titleKeeps.pack(side = "top")
        self.encryptKeepsButton.pack(side = "top")
        self.decryptKeepsButton.pack(side = "top")
        self.generateButton.pack(side = "top")
        self.importButton.pack(side = "top")
        self.backButton.pack_forget()
        self.nameDicLab.pack_forget()
        self.nameDicText.pack_forget()
        self.defaultChoice.pack_forget()
        self.alphanumChoice.pack_forget()
        self.caracFrame.pack_forget()
        self.overwriteCase.pack_forget()
        self.saveReadableCase.pack_forget()
        self.validButton.pack_forget()
        self.dictiosFrame.pack_forget()
        self.importDictioButton.pack_forget()
        self.dictioToImport.pack_forget()
        self.updateDictioButton.pack_forget()
        self.deleteDictioButton.pack_forget()
        self.eCommunTextLab.pack_forget()
        self.eCommunTextEnt.pack_forget()
        self.eEncryptTextLab.pack_forget()
        self.eEncryptTextEnt.pack_forget()
        self.eDictioLab.pack_forget()
        self.eDictioToUse.pack_forget()
        self.eEncryptTextButton.pack_forget()
        self.saveInFile.pack_forget()
        self.encryptedTextLab.pack_forget()
        self.encryptedTextL.pack_forget()
        self.dCommunTextLab.pack_forget()
        self.dCommunTextEnt.pack_forget()
        self.dEncryptTextLab.pack_forget()
        self.dEncryptTextEnt.pack_forget()
        self.dDictioLab.pack_forget()
        self.dDictioToUse.pack_forget()
        self.decryptTextButton.pack_forget()
        self.decryptedTextL.pack_forget()
        self.decryptedTextLab.pack_forget()

    def _import(self):
        self.filePath = tkF.askopenfilename(title = "Import other dictionnaries", filetypes = [("Dictionnaries file", ".dct"), ("Readable dictionnaries file", ".rdct"), ("All files", ".*")])
        self.dictioName = re.sub(".(dct|rdct)$", '', self.filePath.split("/")[-1])
        try :
            keep.dictios[self.dictioName] = keep.importDictios(self.dictioName)
            self.dictioToImport.insert("end", self.dictioName)
        except FileNotFoundError :
            pass

    def delDictio(self):
        try :
            self.dictioName = self.dictioToImport.get(self.dictioToImport.curselection())
        except tk.TclError :
            return False
        keep.removeDictio(self.dictioName)
        self.dictioToImport.delete(self.dictioToImport.curselection())


    def updateDictio(self):
        try :
            self.dictioName = self.dictioToImport.get(self.dictioToImport.curselection())
        except tk.TclError :
            return False
        keep.allDictio.remove(self.dictioName)
        keep.generateDictio(True, keep.dictios.get(self.dictioName).get("settings").get("saveReadable"), self.dictioName, keep.dictios.get(self.dictioName).get("settings").get("alpha"), keep.dictios.get(self.dictioName).get("settings").get("alphaHash"), keep.dictios.get(self.dictioName).get("settings").get("carac"))

    def _fileToSave(self):
        return tk.filedialog.asksaveasfilename(title = "Save encrypted text", filetypes = [("Text file", "*.txt"), ("All file", "*.*")])

clg.debugLevel()

win = tk.Tk()
win.title("KEEP S or AS")
display = Display(win)
_kTk.window = display
win.mainloop()
