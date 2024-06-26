# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:01:43 2023

@author: ramsa
"""

f=open("cyril.txt")
n=m=0
for i in f:
    for j in i:
        if j in "aeiou":
            m+=1
        else:
            n+=1
print(m)
print(n)
f.close()