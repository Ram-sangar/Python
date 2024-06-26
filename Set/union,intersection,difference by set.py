# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:34:33 2022

@author: ramsa
"""

a=set()
b=set()
n=int(input('n='))
for i in range (n):
    c=int(input('c='))
    a.add(c)
for i in range (n):
    d=int(input('d='))
    b.add(d)
e=a.union(b)
f=a.intersection(b)
g=a.difference(b)
print(e)
print(f)
print(g)