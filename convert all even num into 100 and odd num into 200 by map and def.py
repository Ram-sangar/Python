# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:38:31 2023

@author: ramsa
"""

import random as rd
def num(x):
    if(x%2==0):
        return(100)
    else:
        return(200)
a=[rd.randint(0,100) for i in range (200)]
b=map(lambda x:num(x),a)
print(list(b))