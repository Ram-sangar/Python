# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:06:55 2022

@author: ramsa
"""

import random as rd
n=int(input("n="))
a=[rd.randint(-100,200) for i in range(n)]
b=set(a)
c=len(b)
print(a,b,c)
dic={}
for i in b:
    d=a.count(i)
    dic[i]=d
for z in dic:
    print(z,dic[z])