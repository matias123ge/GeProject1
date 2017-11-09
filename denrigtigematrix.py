# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:38:36 2017

@author: matia
"""

import numpy as np
import os
def dataLoad(filename):
    #import matrix
    matrix=np.loadtxt(filename,delimiter=" ")
    #loop for first column, if an error is detected an error message is displayed and the number of the with the error is copied to an index vector
    index=np.array([])
    for i in range (len(matrix)): 
        if (matrix[i,0]<10) or (matrix[i,0]>60) :
            print("Temperature must be a valid number between 10-60, error in column 1 row {:f}".format(i))
            print("")
            index=np.hstack((index,np.array([i])))
        else:
            pass
    #loop for second column, error message if wrong data and insert row number in index vector
    for i in range (len(matrix)): 
        if matrix[i,1]<0:
            print("Bacteria Growth Rate must be a number higher than or equal to 0, error in column 2 row {:f}".format(i))
            print("")
            index=np.hstack((index,np.array([i])))
        else:
            pass
    #loop for third column, error message if wrong data and copy row number in index vector  
    for i in range (len(matrix)): 
        if matrix[i,2]<1 or matrix[i,2]>4:
            print("Bacteria Category must be 1,2,3 or 4, error in column 3 row {:f}".format(i))
            print("")
            index=np.hstack((index,np.array([i])))
        else:
            pass
        #make float values in the index vector to integers
    t=index.astype(int)
    #delete potential dublicate rows
    newind=([])
    for i in t:
        if i not in newind:
            newind.append(i)
    #delete the rows with errors from the origal matrix, and make the matrix called data        
    data=np.delete(matrix,newind,axis=0)         
    return data
    
    