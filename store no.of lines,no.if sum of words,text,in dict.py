# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:26:17 2023

@author: ramsa
"""

f=open("cyril.txt")
dic={}
m=1
for i in f:
    dic[m]=[len(i),i]
    m+=1
print(dic,end="  ")