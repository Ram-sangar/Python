# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:33:40 2023

@author: ramsa
"""

from functools import reduce
import random as rd
a=[rd.randint(1,100) for i in range(100)]
print(a)
b=reduce(lambda x,y:x*y,a)
print(b)