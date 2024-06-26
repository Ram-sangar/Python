# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 09:25:35 2023

@author: ramsa
"""

f=open("cyril.txt")
n=0
dic={}
m=1
for i in f:
    dic[m]=[n,i]
    a=len(i)+1
    n+=a
    m+=1
j=len(dic)   
for i in dic:
    print(i,dic[i])
for i in range(j+1):
    if i%2!=0:

     print(dic[i][1])