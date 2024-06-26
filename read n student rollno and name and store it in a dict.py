# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:34:17 2022

@author: ramsa
"""

n=int(input("n="))
dic={}
for i in range(n):
    rollno=int(input("rollno="))
    name=input("name=")
    dic[rollno]=name
    print(dic)