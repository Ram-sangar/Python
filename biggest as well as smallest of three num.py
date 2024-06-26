# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:17:14 2022

@author: ramsa
"""

def num(a,b,c):
    d=a if a>c else c if a>b else b if b>c else c
    e=a if a<c else c if a<b else b if b<c else c
    return(d,e)
#main
x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
h=num(x,y,z) 
print("big",h,"small")   