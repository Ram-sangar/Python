# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 11:20:45 2023

@author: ramsa
"""

a=lambda r:3.14*r**2
print(a(35))
b=lambda r:4/3*3.14*r**3
print(b(55))
c=lambda r,h:3.14*r**2*h
print(c(233,47))
d=lambda a,b,c:(a if a>c else c) if a>b else (b if b>c else c)
print(d(20,43,10))
d=lambda a,b,c:(a if a<c else c) if a<b else (b if b<c else c)
print(d(23,43,20))
