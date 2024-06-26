# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:01:18 2022

@author: ramsa
"""
import random as rd
l=[rd.randint(100,200) for i in range(10)]
t=tuple(l)
for i in range(len(t)):
    print(t[i])