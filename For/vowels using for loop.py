# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:14:13 2022

@author: ramsa
"""
s=input('s=')
l=len(s)
a=0
b=0
for i in range (l):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        a=a+1
    else:
        b=b+1
print(a)
print(b)