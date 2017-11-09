# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:43:48 2017

@author: Valdemar
"""

import numpy as np
from displayMenu import *

# Define menu items
menuItems = np.array(["Enter name", "Display greeting", "Quit"])
# Define empty name variable
name = ""
# Start
while True:
# Display menu options and ask user to choose a menu item
    choice = displayMenu(menuItems)
# Menu item chosen
# ------------------------------------------------------------------
# 1. Enter name
    if choice == 1:
# Ask user to input name and save it in variable
        name = input("Please enter your name: ")
# ------------------------------------------------------------------
# 2. Display greeting
    elif choice == 2:
# Is name empty?
        if name == "":
# Display error message
            print("Error: Name is empty")
        else:
# Display greeting
            print("Hello {:s}".format(name))
# ------------------------------------------------------------------
# 3. Quit
    elif choice == 3:
# End
        break