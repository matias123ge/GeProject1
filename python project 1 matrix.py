# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:58:53 2017

@author: matia
"""
import numpy as np
import os
def dataLoad(filename):
    #open and read datafile
    numbers=open(filename, 'r')
    #convert into a vector without \n
    for line in numbers.readlines():
        matrix= map(int, line.split())
        np.append(matrix)
    #converts file into a numpy array forsøg 2 
    vector=np.asarray(numbers)
    
    #convert into matrix
    len(numbers)
    
    
    
    
    
    return data