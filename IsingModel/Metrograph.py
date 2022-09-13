#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:21:11 2022

@author: thales
"""
import matplotlib.pyplot as plt 
import numpy as np
import math
import Metropolis as Metro

def TakeAPic(lattice):
    Array = np.resize(lattice.array,(lattice.size,lattice.size))
    return plt.pcolor(Array)



def main():
    lattice = Metro.Lattice(2,100)
    a=[]
    for i in range(10000):
        lattice.step()
    if i%1000 ==0:
        a +=TakeAPic(lattice)


    return 

if __name__== "__main__":
    main()