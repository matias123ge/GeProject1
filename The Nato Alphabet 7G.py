# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:54:56 2017

@author: Aimas
"""

import numpy as np

def textToNato(plainText):
    #define the letters in the alphabet
    alphabet = np.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    #define NATO alphabet in array
    Nato = np.array(["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","Xray","Yankee","Zulu"])
    lower_txt = plainText.lower() #make the input text lower case
    
    chrList = np.asarray(list(lower_txt)) #make the characters of the word into elements of an array
    final_array = np.array([]) 
    for i in range(len(lower_txt)): #make a loop that checks every letter in the given word, and replaces it with NATO alphabet
        check_alfb = np.where(chrList[i] == alphabet)
        if len(final_array) == 0:
            final_array = Nato[check_alfb[0]][0]
        else:
            final_array = np.hstack((final_array, Nato[check_alfb[0]][0]))
    final_txt = "-".join(final_array) #join the array of NATO-letters and seperate with "-"
        
    return final_txt