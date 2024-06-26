# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 10:27:00 2022

@author: ramsa
"""
n=int(input('n='))
dic={}
for i in range (n):
    rollno=int(input('rollno='))
    name=input('name=')
    age=int(input('age='))
    Class=input('class=')
    email=input('email=')
    dic[rollno]=[name,age,Class,email]
for i in dic:
    print(i,dic[i])