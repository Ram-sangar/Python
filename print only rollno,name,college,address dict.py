# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 10:40:53 2022

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
    address=input('address=')
    dic[rollno]=[name,age,Class,email,address]
for i in dic:
    print(i,dic[i][0],dic[i][1],dic[i][4])