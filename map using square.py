# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:43:29 2023

@author: ramsa
"""

import random as rd
n=int(input("n="))
a=[rd.randint(0,20) for i in range (n)]
b=map(lambda x:x**2,a)
print(list(b))
