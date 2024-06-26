# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:06:51 2023

@author: ramsa
"""

f=open("cyril.txt")
m=1
for i in f:
    print(m,i,end="")
    m+=1
f.close()