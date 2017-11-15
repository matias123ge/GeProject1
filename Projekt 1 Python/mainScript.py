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
    print("")
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i])) #Display menu options
    #Get a userinput to determine which function to execute
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        try:
            choice = float(input("Please choose a menu item: ")) #Choose in the menu.
            if choice < 0: #Make an exception that does not allow for negative numbers
                raise ValueError
            else:
                pass
        except ValueError:
            print("That is not a valid number, dude!")
            choice = 0
            
    #Menu item chosen
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
        #Show second menu that gives you the differnet types of statistics available
        choice = 0
        options2 = np.array(["Mean Temperature","Mean Growth Rate","Std Temperature","Std Growth Rate", "Rows","Mean Cold Growth Rate", "Mean Hot Growth Rate","Return"])
        while not(np.any(choice == np.arange(len(options2))+1)): #make a while loop, that stays in the statistics menu, until the user wishes to return to the main menu
            try:
                print("-------------------------------------------------")
                print("Please type the number corresponding to the statistic or action you desire, as stated in the list below:")
                for i in range(len(options2)):
                    print("{:d}. {:s}".format(i+1, options2[i])) #Display menu options
                choice = int(input("Please enter your desired action: "))
                statistics = options2[choice-1]
                if np.any(choice == np.array([1,2,3,4,5,6,7])): 
                    stats = dataStatistics(data, statistics)
                    print("")
                    print("Calculated value: {:f}".format(stats))
                    print("") #print the statistic
                    choice = 0
                elif choice == 8:
                    break
                elif choice < 0: #raise a value error for negative numbers
                    raise ValueError
            except IndexError:
                    print("An ERROR OCCURED: Please pick a valid number.")
            except ValueError:
                    print("An ERROR OCCURED: Please pick a valid number.")
                    
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