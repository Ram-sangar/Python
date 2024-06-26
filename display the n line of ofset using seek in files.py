# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:11:51 2023

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
print(dic)
n=int(input("n="))
f.seek(dic[n][0])
a=f.readline()
print(a)
f.close()
