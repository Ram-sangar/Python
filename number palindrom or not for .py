# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:07:50 2022

@author: ramsa
"""

a=int(input('a='))
s=str(a)
l=len(s)
s2=""
for i in range (1,l+1):
    s2+=s[-i]
b=int(s2)
if(a==b):
    print(b,'palindrom')
else:
    print(b,'not palindrom')
    