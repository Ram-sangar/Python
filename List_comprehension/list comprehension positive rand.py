# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:36:41 2022

@author: ramsa
"""
import random as rd
b=[]
a=[rd.randint (-100,100) for i in range(0,100)]
b.append(a)
b=[i for i in a if(i>0)]
print(b)