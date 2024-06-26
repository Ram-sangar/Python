# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 11:44:30 2023

@author: ramsa
"""
f=open("cyril.txt","r")
e=open("yogi.txt","w")
h=open("arul.txt","w")
dic={}
n=0
m=1
for i in f:
    dic[m]=n
    a=len(i)+1
    n+=a
    m+=1
    b=len(dic.values())
for i in range (1,b+1):
    if(i%2==0):
        f.seek(dic[i])
        c=f.readline()
        d=e.write(c)
        print(d)
    else:
        f.seek(dic[i])
        c=f.readline()
        d=h.write(c)
        print(d)
e.close()

    
h.close()
f.close()
