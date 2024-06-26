# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 12:13:40 2023

@author: ramsa
"""

f=open("cyril.txt")
dic={}
m=1
n=0
for i in f:
    dic[m]=[n,i]
    a=len(i)
    n=a+n
    m+=1
print(dic)