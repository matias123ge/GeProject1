# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:38:58 2017

@author: Valdemar
"""

import numpy as np
from inputNumber import inputNumber
def displayMenu(options):

    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))

    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
    return choice
