# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 10:08:50 2022

@author: ramsa
"""

import random as rd
a=[rd.randint(-100,200) for i in range(1000)]
b=len(a)
c=set(a)
d=len(c)
e=b-d
print(a)
print(c)
print(b)
print(d)
print(e)