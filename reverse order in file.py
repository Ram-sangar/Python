# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:57:48 2023

@author: ramsa
"""

f=open("cyril.txt")
dic={}
n=0
m=1
for i in f:
    dic[m]=n
    a=len(i)+1
    n+=a
    m+=1
c=len(dic.values())
for i in range (c,1,-1):
    f.seek(dic[i])
    c=f.readline()
    print(c,end="")
f.close()