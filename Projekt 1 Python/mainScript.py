# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 13:52:53 2017

@author:
"""
import numpy as np
from dataPlot import * 
from dataStatistics import * 
from dataLoad import *

# Start
print("")
print("Welcome to your favourite Bacterial Growth calculator. Please type a number corresponding to your desired action:")
# Defining menu options
options = np.array(["Load data", "Filter data", "Display statistics", "Generate plots", "Quit"])
while True:   
    print("-------------------------------------------------")
    for i in range(len(options)):
        print("")
        print("{:d}. {:s}".format(i+1, options[i])) #Display menu options
    #Get a userinput to determine which function to execute
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        try:
            choice = float(input("Please choose a menu item: ")) #Choose in the menu. 
        except ValueError:
            print("That is not a number, dude!")
            choice = 0
# Menu item chosen
    if choice == 1: #Load data if input is 1
        try:
            print("")
        #define the filename you want to input
            filename = input("Please enter the name of the file you want to load: ")
            print("")
            data = dataLoad(filename)
        except FileNotFoundError:
            print("The file is not found. Please check if your typed correctly or if the file exists in the folder.")
    elif choice == 2: #Additional filtering if input is 2
        print("")
        print("Lol nope...")
    elif choice == 3: #Open statistics menu, if input is 3
        try:
            #Show second menu that gives you the differnet types of statistics available
            print("----------")
            options2 = np.array(["Mean Temperature","Mean Growth Rate","Std Temperature","Std Growth Rate", "Rows","Mean Cold Growth Rate", "Mean Hot Growth Rate","Return"])
            print("Please type the following type of statistic or action you desire, as stated in the list below:")
            for i in range(len(options2)):
                print("")
                print("- {:s}".format(options2[i])) #Display menu options
            statistics = input("Please enter your desired action: ")
            stats = dataStatistics(data, statistics)
            print("")
            print("Calculated value:")
            print(stats) #print the statistic
        #except UnboundLocalError:
            #print("An ERROR OCCURED: Please load data using the 'Load data' function.")
        except NameError:
            if statistics.lower() == "return":
                pass
            else:
                print("An ERROR OCCURED: Please check if you loaded any data or spelled the action correctly.")
    elif choice == 4: #Plot data if input is 4
        print("")
        try:
            plot = dataPlot(data)
            print(plot)
        except NameError:
            print("An ERROR OCCURED: Please load data using the 'Load data' function")
    elif choice == 5: #Close the script, if input is 5
        print("")
        print("Ciaooo bella!")
        break