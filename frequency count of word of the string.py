# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 10:10:20 2022

@author: ramsa
"""

s=input("s=")
l=s.split()
a=list(l)
b=set(a)
for i in b:
    d=a.count(i)
    print(d)