# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:14:40 2022

@author: ramsa
"""

import random as rd
n=int(input("Enter the number:"))
l=[rd.randint(10000,50000) for i in range(n)]
t=tuple(l)
b=c=t[0]
p=q=0
for i in range (len(t)):
    if b<t[i]:
        b=t[i]
        p=i
    elif c>t[i]:
        c=t[i]
        q=i
print(b)
print(c)
        