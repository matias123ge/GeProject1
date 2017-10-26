# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:45:13 2017

@author: Aimas, Matias og Valdemar
"""
import numpy as np

def dataStatistics(data, statistic):
    #Columns in matrix are Temperature, Growth rate, and Bacteria.
    statistic = statistic.lower() #Correct user input to lower case string
    #Calculate average temperature
    if statistic == "mean temperature":
        result = np.mean(data[:,0])
    #Calculate average growth rate
    elif statistic == "mean growth rate":
        result = np.mean(data[:,1])
    #Calculate standard temperature
    elif statistic == "std temperature":
        result = (np.std(data,axis=1))[0] #use np.std to find std. dev. and choose first column 
    #Calculate standard growth
    elif statistic == "std growth rate":
        result = (np.std(data,axis=1))[1] #use np.std to find std. dev. and choose second column 
    #Calculate number of rows
    elif statistic == "rows":
        result = len(data[:,0])
    #Calculate average growth rate when T < 20
    elif statistic == "mean cold growth rate":
        try:
            data = data[np.where(data[:,0] < 20)] #find the rows in the matrix that satisfies the given interval
            result = np.mean(data[:,1]) #take the average value of the remaining column
        except #noget med NaN: #if there is no temperature <20, return error message
            print("No temperature lower than 20 degrees.")           
    #Calculate average growth rate when T > 50
    elif statistic == "mean hot growth rate":
        try:
            data = data[np.where(data[:,0] > 50)] #find the rows in the matrix that satisfies the given interval
            result = np.mean(data[:,1]) #take the average value of the remaining column
        except #noget med NaN: #if there is no temperature <20, return error message
            print("No temperature higher than 50 degrees.")
    else:
        print("Input not valid. Try again!")
    
    return result