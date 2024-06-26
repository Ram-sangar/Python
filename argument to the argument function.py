# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 10:10:07 2023

@author: ramsa
"""

def sum(a,b):
    return(a+b)
def minus(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
def exp(a,b):
    return(a**b)
def quo(a,b):
    return(a//b)
def calculate(m,x,y):
    c=m(x,y)
    return(c)
#main
d=calculate(sum,100,200)
e=calculate(minus,13500,200)
f=calculate(mul,185,200)
g=calculate(div,1850,200)
h=calculate(exp,10,2)
i=calculate(quo,1500,200)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
    
