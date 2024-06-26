# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:11:47 2022

@author: ramsa
"""

b=[]
n=3
for i in range (n):
    a=[]
    for j in range (n):
        c=int(input('c='))
        a.append(c)
    b.append(a)   
for i in range (n):
    for j in range (n):
        print(b[i][j],end="")
    print()
        
    