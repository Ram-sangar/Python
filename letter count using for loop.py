# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:21:00 2022

@author: ramsa
"""

s=input('s=')
l=len(s)
a=0
b=0
c=0
for i in range (l):
    if s[i]>='A' and s[i]<='Z':
        a+=1
    elif s[i]>='a' and s[i]<='z':
        b+=1
    else:
        c+=1
print(a)
print(b)
print(c)
        