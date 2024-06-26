# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:10:00 2023

@author: ramsa
"""

import random as rd
def square(x):
    a=x**2
    return(a)
n=int(input("n="))
b=[rd.randint(0, 20) for i in range(n)]
c=map(lambda x:square(x),b)
print(list(c))