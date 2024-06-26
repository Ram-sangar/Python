# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:44:57 2022

@author: ramsa
"""

s=input('s=')
l=len(s)
s2=''
for i in range (l):
    if (s[i]!=','):
        s2+=s[i]
print(s2)