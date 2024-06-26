# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 18:45:25 2022

@author: ramsa
"""

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=(a if a>c else c)if a>b else (b if b>c else c )
e=(a if a<c else c)if a<b else (b if b<c else c )
f=(a+b+c)-d-e
print(d)
print(f)
print(e)
g=[a,b,c]
print(g.sort())