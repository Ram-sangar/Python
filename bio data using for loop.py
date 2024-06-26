# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:36:14 2022

@author: ramsa
"""

n=int(input('n='))
a=[]
for i in range (n):
    name=input('name=')
    rollno=input('rollno=')
    age=int(input('age='))
    p=[name,rollno,age]
    a.append(p)
for i in range(n):
    print(a[i])