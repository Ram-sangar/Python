# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:26:07 2023

@author: ramsa
"""

from functools import reduce
import random as rd
a=[rd.randint(0,100) for i in range(100)]
print(a)
s=reduce(lambda x,y:x+y,a)
print(s)