# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:15:21 2017

@author: s174435
"""

import numpy as np
import matplotlib.pyplot as plt

def dataPlot(data):
    #Sort data w.r.t. temperature increase, to make the line plot watchable
    data = data[np.lexsort((data[:,0], ))]
    #Split the matrix into four matrices for every type of bacteria
    matrix_SE = data[np.where(data[:,2] == 1)] #Salmonella Enterica
    matrix_BC = data[np.where(data[:,2] == 2)] #Bacillus Cereus
    matrix_L = data[np.where(data[:,2] == 3)] #Listeria
    matrix_BT = data[np.where(data[:,2] == 4)] #Brochothrix Thermosphacta
    
    #Data treatment for number of bacteria
    y = np.delete(np.bincount(data[:,2].astype(int)),0) #Count the number of occurrences of each integer in 3rd column of the data matrix
    bacteria = np.array(["Salmonella E.","Bacillus Cereus","Listeria","Brochothrix T."])
    x_pos = np.arange(len(bacteria)) #Define an array that shows the location in the x-direction for the different species
    plt.bar(x_pos, y, align="center", alpha = 0.5)
    plt.xticks(x_pos,bacteria)
    plt.ylabel("Number of occurences")
    plt.title("Plot of occurrences of different bacteria")
    plt.show()
    
    #Data treatment for growth rate by temperature    
    #Define x- and y-data from the different sets of bacteria
    x_SE = matrix_SE[:,0] 
    y_SE = matrix_SE[:,1]
    x_BC = matrix_BC[:,0]
    y_BC = matrix_BC[:,1]
    x_L = matrix_L[:,0]
    y_L = matrix_L[:,1]
    x_BT = matrix_BT[:,0] 
    y_BT = matrix_BT[:,1]
    
    matrixList = np.array([matrix_SE, matrix_BC, matrix_L, matrix_BT]) #make an index for where we find if some data arrays for certain bacteria is empty
    index = np.where(matrixList != 0)
    
    #Specify plots and execute
    plt.plot(x_SE,y_SE, "red")
    plt.plot(x_BC,y_BC,"blue")
    plt.plot(x_L,y_L,"green")
    plt.plot(x_BT,y_BT,"black")
    plt.title("Coorelation between temperature and bacteria growth rate") #Title
    plt.xlabel("Temperature in degrees Celsius") #x-label
    plt.ylabel("Growth rate of bacteria") #y-label
    plt.xlim([10,60]) #limits in the x-direction
    plt.ylim([0,max(data[:,1] + np.mean(data[:,1]/10))]) #limit in the y-direction
    plt.legend(["Salmonella Enterica", "Bacillus Cereus", "Listeria", "Brochothrix Thermosphacta"],loc='center left', bbox_to_anchor=(1, 0.5),fancybox=True) #legend specifications
    plt.show()