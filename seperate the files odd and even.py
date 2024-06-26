# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 11:29:56 2023

@author: ramsa
"""

f=open("cyril.txt","r")
e=open("gill.txt","w")
h=open("hevin.txt","w")
dic={}
n=0
m=1
for i in f:
    dic[m]=n
    a=len(i)+1
    n+=a
    m+=1
print(dic)
b=len(dic.values())
for i in range (1,b+1,2):
        f.seek(dic[i])
        c=f.readline()
        d=e.write(c)
        
        print(d)
e.close()
for i in range(2,b+1,2):
    f.seek(dic[i])
    c=f.readline()
    d=h.write(c)
    print(d)
h.close()
f.close()

    