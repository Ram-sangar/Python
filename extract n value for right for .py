# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:11:46 2022

@author: ramsa
"""

s=input('s=')
n=int(input('n='))
s2=""
for i in range (1,n+1):
    s2=s2+s[-i]
print(s2)