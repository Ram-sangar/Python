# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 09:02:08 2023

@author: ramsa
"""

f=open("cyril.txt")
n=0
dic={}
m=1
for i in f:
    dic[m]=n
    a=len(i)+1
    n+=a
    m+=1
print(dic.values())
b=len(dic.values())
for i in range (1,b+1,2):
    f.seek(dic[i])
    a=f.readline()
    print(a)
f.close()

    

