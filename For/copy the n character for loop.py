# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:45:52 2022

@author: ramsa
"""

s=input('s=')
n=int(input('n='))
s2=""
l=len(s)
q=l-n
for i in range (q,l):
    s2+=s[i]
print(s2)