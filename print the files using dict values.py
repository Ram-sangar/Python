# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:35:47 2023

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
b=dic.values()
print(b)
for i in b:
    f.seek(i)
    a=f.readline()
    print(a)
f.close
    
