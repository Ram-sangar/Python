# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:48:55 2023

@author: ramsa
"""

f=open("cyril.t1xt")
m=1
for i in f:
    if(m%10==0):
        int(input("m="))
    else:
        print(m,i)
    m+=1
f.close()