# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 10:33:19 2022

@author: ramsa
"""

import random as rd
n=int(input("n="))
a=[rd.randint(-100,50) for i in range (n)]
b=set(a)
c=len(b)
e=len(a)
print(a)
print(b)
print(c,e)
for i in b:
    d=a.count(i)
    print(i,d)