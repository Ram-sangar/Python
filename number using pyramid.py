# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:47:33 2023

@author: ramsa
"""

a=1
b=2
c=3
for i in range(c):
    for j in range(1,b):
        print(a,end=" ")
        a+=1
    print()
    b+=2

a=11
b=2
c=6
for i in range(c):
    for j in range(1,b):
        print(a-j,end=" ")
    print()
    b+=1
a=10
b=1
c=4
for i in range(c):
    for j in range(0,b,2):
        print(a-j,end=" ")
        b+=1
    print()
    b+=1



