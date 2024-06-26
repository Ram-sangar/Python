# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:36:43 2022

@author: ramsa
"""

s=input('s=')
n=int(input('n='))
m=int(input('m='))
s2=""
q=n+m
for i in range (m,q):
    s2+=s[i]
print(s2)