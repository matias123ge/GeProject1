# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:35:06 2017

@author: matia
"""
import numpy as np
import os
import matplotlib.pyplot as plt
conditions=np.array([1,2,3,4,5])
def print_menu():
    print("Welcome to Bacteria Infomator9000! What do you want to do?")
    print("1. Load Data")
    print("2. Filter Data")
    print("3. Display Statistics")
    print("4 Generate Plots")
    print("5. Quit")
loop=True 
while loop: 
    print_menu()
    try:
        choice= float(input(" Enter a number between [1-5]:"))
    except ValueError:
        print("Not a valid number, please try again.")
        print("")
        choice=0
    if choice==1: 
        filename=input("Please enter a filename you want to load: ")
        
          
        
    elif choice==2:
        #menu options of different bacteria filters
        print("1. Salmonella enterica")
        print("2. Bacillus cereus")
        print("3. Listeria")
        print("4. Brochothrix thermosphacta")
        print("5. All bacteria")
        bact=float(input("Enter bacteria type nr."))
        #start data from subscript 1
        data=data
        #define while bacteria number is 1,2,3,4,5 what to do:
        while bact==np.any(conditions):
        #sort away all bacteria except type 1:
            if bact==1 :
                for i in range (len(data)):
                    if data[i,2]!=1:
                        index=np.hstack((index,np.array([i])))
                    else:
                        pass
                    t=index.astype(int)
                    newind=([])
                    for i in t:
                            if i not in newind:
                                    newind.append(i)     
                    data1=np.delete(data,newind,axis=0)     
            #sort away all data except type 2
            elif bact==2 :
                for i in range (len(data)):
                    if data[i,2]!=2:
                        index=np.hstack((index,np.array([i])))
                    else:
                        pass
                t=index.astype(int)
                newind=([])
                for i in t:
                    if i not in newind:
                        newind.append(i)     
                    data2=np.delete(data,newind,axis=0)  
            #sort away all data except type 3
            elif bact==3 :
                for i in range (len(data)):
                    if data[i,2]!=3:
                        index=np.hstack((index,np.array([i])))
                    else:
                        pass
                t=index.astype(int)
                newind=([])
                for i in t:
                    if i not in newind:
                        newind.append(i)     
                    data3=np.delete(data,newind,axis=0) 
            #sort away all data except type 4
            elif bact==4 :
                for i in range (len(data)):
                    if data[i,2]!=4:
                        index=np.hstack((index,np.array([i])))
                    else:
                        pass  
                t=index.astype(int)
                newind=([])
                for i in t:
                    if i not in newind:
                        newind.append(i)     
                    data4=np.delete(data,newind,axis=0)  
            #keep all data 
            elif bact==5 :
                data=data
            else:
                print("Please input a valid bacteria category")
                pass 
            print("Do you want to specify a growth rate?")
            YN=float(input("1. Yes 2. No"))
            if YN==1:
                GR=(float(input("Please enter a growth rate between 0,5 and 1")))
                if bact=1:
                     for i in range (len(data1)): 
                         if data1[i,1]<GR:
            index=np.hstack((index,np.array([i])))
        else:
            pass
                
                
            if YN==2:
                pass
            
            
    elif choice== 3: 
        print("noshit")
        print("")
    elif choice== 4: 
        print("fuckprogmas")
        print("")
    elif choice==5:
        print("Goodbye")
        break
    
    