# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:15:40 2022

@author: ramsa
"""
s=input('s=')
l=len(s)
s2=""
for i in range(1,l+1):
    s2=s2+s[-i]
if(s==s2):
    print(s2,'palindrom')
else:
    print(s2,'not palindrom')
