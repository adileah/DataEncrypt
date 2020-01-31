# -*- coding: utf-8 -*-

#iostream

import sys

def Encrypt(key, file):
    #check for key and file
    if isinstance(key, str) and isinstance(file, str):
        #create array of words
        f = open(file)
        text = f.readlines()
        stringList = []
        newLine = []
        chopLine = []
        for x in text:
            stringList.append(x)
        print(stringList)
        for x in stringList:
            line =  list(x)
            for y in line:
                if(y.isalpha()): 
                    newLine.append(y)
                else:
                    newLine.append(y)
        print(newLine)
        i = 0
        while i < (len(newLine)-1):
            if(newLine[i].isalpha() and newLine[i+1].isalpha()):
                chopLine.append(newLine[i] + newLine[i+1])
                i += 2
            elif(newLine[i].isalpha()):
                chopLine.append(newLine[i] + 'z')
                chopLine.append(newLine[i+1])
                i += 2
            else:
                chopLine.append(newLine[i])
                i += 1
        print(chopLine)
        #create key
        keyTable = makeKey(key)
        print(keyTable)
        #create empty coded text string
        codedText = ""     

    else:
    	print("give me a key and then the name of your file ")

def makeKey(key):
    keyTable = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in key.upper():
        if char not in keyTable and char in alphabet:
            keyTable.append(char)
    for char in alphabet:
        if char not in keyTable:
            keyTable.append(char)
    return keyTable

Encrypt(sys.argv[1],sys.argv[2])















