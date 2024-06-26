# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:29:31 2022

@author: ramsa
"""

n=int(input("n="))
a=[]
for i in range (n):
    name=input("name =")
    age=int(input("age ="))
    rollno=(input("rollno ="))
    p=[name,age,rollno]
    a.append(p)
t=tuple(a)
for i in range (len(t)):
       print(t[i])    