# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:51:02 2022

@author: ramsa
"""

import random as rd
n=int(input("n="))
a=[rd.randint(-100,200) for i in range(n)]
b=set(a)
print(a)
print(b)