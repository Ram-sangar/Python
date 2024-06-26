# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:24:44 2023

@author: ramsa
"""

a=1
b=0
c=0
while a<10:
    if a%2==0:
        b=a+b
    else:
        c+=a
    a+=1
print(b,c)
