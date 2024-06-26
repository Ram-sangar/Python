# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:12:55 2023

@author: ramsa
"""

def word(a):
    b=0
    c=0
    for i in a:
        if i in 'aeiou':
            b+=1
        else:
            c+=1
    return(b,c)
#main
a=input("a=")
b=word(a)
print(b)
            