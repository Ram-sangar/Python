# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:53:31 2023

@author: ramsa
"""

f=open("cyril.txt")
n=0
dic={}
m=1
for i in f:
    dic[m]=[n]
    a=len(i)+1
    n+=a
    m+=1
print(dic.values())
d=len(dic.values())
print(d)
for i in range(1,d+1,2):
    f.seek(dic[i])
    a=f.readline()
    print(a)
    