# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:29:15 2022

@author: ramsa
"""
import random as rd
n=3
a=[[rd.randint(1000,2000) for j in range(n)]for i in range(n)]
t=tuple(a)
for i in t:
    for j  in i:
      print(j,end=" ")
    print()
        
        