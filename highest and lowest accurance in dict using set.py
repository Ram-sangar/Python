# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 09:24:48 2022

@author: ramsa
"""

import random as rd 
n=int(input("n ="))
a=[rd.randint(-100,200) for i in range (n)]
b=set(a)
c=len(b)
print(a,b,c)
dic={}
for i in b:
    d=a.count(i)
    dic[i]=d
f=0
e=dic[0]
for z in dic:
    print(z,dic[z])
    if f<dic[z]:
        f=dic[z]
        x=z
    elif e>dic[z]:
        e=dic[z]
        y=z
print("highest accurance :",f)
print("highest accurance key is :",x)
print("lowest accurance :",e)
print("lowest accurance key is :",y)