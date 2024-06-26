# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:19:31 2022

@author: ramsa
"""

s=input('s=')
l=len(s)
a=0
b=0
for i in range (l):
    if s[i] in 'aeiou':
        a=a+1
    else:
        b=b+1
print(a)
print(b)