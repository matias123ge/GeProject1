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
options = np.array(["Load data", "Filter data", "Display statistics", "Generate plots","Show Data","Clear Filters", "Quit"])
#Variable used to decide whether or not to clear filters.
aimas=3
#Start the menu
while True:   
    print("")
    print("-------------------------------------------------")
    print("")
    #Display active filters, if any
    if "countarrayfinal" in locals():
        print("Active filters:")
        print(countarrayfinal)
    if "LB" in locals():
        print("Growth filters")
        print("Lower bound {}".format(LB))
        print("Upper bound {}".format(UB))
    #Display menu options
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    #Get a userinput to determine which function to execute
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        try:
            #Choose in the menu.
            choice = float(input("Please choose a menu item: ")) 
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
            #Variable to return to original data set.
            databackup=data
        except FileNotFoundError:
            print("The file is not found. Please check if your typed correctly or if the file exists in the folder.")
    elif choice == 2: #Additional filtering if input is 2
        # Check wheter or not data has been loaded before filtering
        if "databackup" not in locals():
            print("An ERROR OCCURED: Please load data using the 'Load data' function")
            pass
        elif "databackup" in locals():
            #Define filter options for Bacteria type
            choice=0
            options3 = np.array(["1. Salmonella enterica","2. Bacillus cereus","3. Listeria","4. Brochothrix thermosphacta", "5. All bacteria","6. Choose growth filter","7. Continue without growth filer","8. Return to main menu", "9. Remove current growth filter"])
            #Arrays to filter in
            data1=np.array([0,0,0])
            data2=np.array([0,0,0])
            data3=np.array([0,0,0])
            data4=np.array([0,0,0])
            countarray1=np.array([])
            countarray2=np.array([])
            countarray3=np.array([])
            countarray4=np.array([])
            countarray5=np.array([])
            print("----------")
            #Start of filter loop
            for i in range(len(options3)):
                print(" {:s}".format(options3[i]))
            while not(np.any(choice ==np.arange(len(options3))+1)):
                try:
                    choice= int(input("Enter the number corresponding to bacteria type or option:"))
                    #Filter choice after user input
                    if choice==1:
                        data1=databackup[np.where(databackup[:,2]==1)]
                        countarray1=options3[choice-1]
                        choice=0
                    elif choice==2:
                        data2=databackup[np.where(databackup[:,2]==2)]
                        countarray2=options3[choice-1]
                        choice=0
                    elif choice==3:
                        data3=databackup[np.where(databackup[:,2]==3)]
                        countarray3=options3[choice-1]
                        choice=0
                    elif choice==4:
                        data4=databackup[np.where(databackup[:,2]==4)]
                        countarray4=options3[choice-1]
                        choice=0
                    elif choice==5:
                        data=databackup
                        countarray5=options3[choice-1]
                        countarrayfinal=countarray5
                        break
                    elif choice==6 or choice==7:
                        #Variable to definer whether or not filters can be cleared:
                        aimas=1
                        #Make the final array with the filtered data and print types chosen.
                        countarrayfinal=np.hstack((countarray1,countarray2,countarray3,countarray4))
                        print("These options have been chosen:")
                        print(countarrayfinal)
                        datafinal=np.vstack((data1,data2,data3,data4))
                        data=np.delete(datafinal,np.where(datafinal[:,2]<1),axis=0)
                        databackup1=np.delete(datafinal,np.where(datafinal[:,2]<1),axis=0)
                        break
                    elif choice==8 :
                        break
                    #Make user unable to remove growth boundaries if there are none:
                    elif choice==9:
                        if "LB" in locals(): 
                            data=databackup1
                            del(LB)
                            break
                        elif "LB" not in locals():
                            print("AN ERROR OCCURED: No current growth boundaries")
                            break
                    elif choice < 0:
                        raise ValueError
                except IndexError:
                        print("An ERROR OCCURED: Please pick a valid number.")
                except ValueError:
                        print("An ERROR OCCURED: Please pick a valid number.")
            while True:
                if choice==7 or choice==8 or choice == 9:
                    break 
                try:
                    #Insert lower and 
                    LB=float(input("Please insert you lower bound:"))
                    UB=float(input("Please insert you upper bound:"))
                    data=data[np.where(np.logical_and(data[:,1]>LB, data[:,1]<UB))]
                    aimas=2
                    break
                except ValueError:
                    print("That is not a number, dude!")
                pass
            
    elif choice == 3: #Open statistics menu, if input is 3
        #Show second menu that gives you the different types of statistics available
        if "databackup" not in locals():
            print("An ERROR OCCURED: Please load data using the 'Load data' function")
            pass
        elif "databackup" in locals():
            choice = 0
            options2 = np.array(["Mean Temperature","Mean Growth Rate","Std Temperature","Std Growth Rate", "Rows","Mean Cold Growth Rate", "Mean Hot Growth Rate","Return"])
            while not(np.any(choice == np.arange(len(options2))+1)): #make a while loop, that stays in the statistics menu, until the user wishes to return to the main menu
                try:
                    print("-------------------------------------------------")
                    print("Please type the following type of statistic or action you desire, as stated in the list below:")
                    for i in range(len(options2)):
                        print("{:d}. {:s}".format(i+1, options2[i])) #Display menu options
                    choice = int(input("Please enter your desired action: "))
                    statistics = options2[choice-1]
                    if np.any(choice == np.array([1,2,3,4,5,6,7])):
                        stats = dataStatistics(data, statistics)
                        print("")
                        print("Calculated value:")
                        print(stats) #print the statistic
                        choice = 0
                    elif choice == 8:
                        break
                    elif choice < 0:
                        raise ValueError
                #except UnboundLocalError:
                    #print("An ERROR OCCURED: Please load data using the 'Load data' function.")
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
    elif choice ==5:
        print("")
        print(data)
    elif choice == 6: #Clear data filters 
            if aimas==1:
                del(countarrayfinal)
                del(aimas)
                print("Filters Cleared")
                data=databackup
            elif aimas==2:
                del(LB)
                del(UB)
                del(countarrayfinal)
                del(aimas)
                print("Filters Cleared")
                data=databackup
            elif aimas==3:
                print("No active filters")
                pass
    elif choice ==7:
        print("")
        print("Ciaooo bella!")
        break