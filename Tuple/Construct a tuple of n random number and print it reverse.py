# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:51:35 2023

@author: ramsa
"""

import random as rd
n=int(input("enter a number:"))
l=[rd.randint (100,200) for i in range (n)]
t=tuple(l)
for i in range (1,len(t)+1):
    print(t[-i],end=' ')