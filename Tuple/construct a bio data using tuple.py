# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 22:01:38 2023

@author: ramsa
"""

        
n=int(input("n="))
a=[]
for i in range (n):
    name=input("name:")
    age=input("age:")
    dno=input("dno:")
    p=[name,age,dno]
    a.append(p)
t=tuple(a)
print(t)
for i in range(len(t)):
    print(t[i])