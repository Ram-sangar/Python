# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:19:26 2022

@author: ramsa
"""

dic={}
n=int(input('n='))
for i in range (n):
    rollno=int(input('rollno='))
    name=input('name=')
    age=int(input('age='))
    Class=input('class=')
    email=input('email=')
    dic[rollno]=[name,age,Class,email]
    for i in dic:
        print(i,dic[i])