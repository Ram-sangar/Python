# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:08:30 2022

@author: ramsa
"""
import random as rd
l=[rd.randint(1000,2000) for i in range(10)]
t=tuple(l)
for i in range(1,len(t)):
    print(t[-i])