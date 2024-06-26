# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 12:09:46 2022

@author: ramsa
"""


def sum (*a):
    c=0
    for i in a:
        c+=i
    return(c)
a=sum(10,20)  
b=sum(1,2,3,7,4,8,9,10,11,12)
c=sum(10,20,302,3,4,12,15,42,45,2,5324,5,45,4)
print(a)
print(b)
print(c)