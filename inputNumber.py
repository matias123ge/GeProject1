# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:58:19 2017

@author: Valdemar
"""
def inputNumber(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
        return num




