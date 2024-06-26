# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:23:39 2023

@author: ramsa
"""
import random as rd 
n=int(input("n="))
a=[rd.randint(0,1000) for i in range(n)]
b=filter(lambda x:x>9 and x<100,a)
print(list(b))
