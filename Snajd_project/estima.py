#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:33:01 2023

@author: thales
"""
import math as mt
import random as rd

print("Este programa é um teste!")

n = int(input("Diga um número"))
counter = 0
total  = 0
for i in range (n):
    number1 = rd.random()
    number2 = rd.random()
    if (number1**2 + number2**2 < 1):
        counter+= 1
    total += 1

print(counter*4/total)
 