# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:00:03 2023

@author: ramsa
"""

f=open("cyril.txt")
n=0
dic={}
m=1
for i in f:
    dic[m]=[n,i]
    a=len(i)
    n+=a
    m+=1
n=int(input("n="))
m=int(input("m="))

print(dic[n][0],dic[n][1])
print(dic[m][0],dic[m][1])
f.seek(dic[n][0])
a=f.readline()
print(a)
f.close()