# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:32:54 2023

@author: ramsa
"""

f=open("cyril.txt")
dic={}
m=1
n=0
a=0
for i in f:
    dic[m]=[len(i),i]
    m+=1
for i in dic:
    if dic[i][0]>n:
        n=dic[i][0]
        a=i
print(a,n,dic[a][1])
f.close()
        