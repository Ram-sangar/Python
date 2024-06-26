# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:59:42 2023

@author: ramsa
"""

b=c=0
def word(a):
    global b,c
    for i in a:
        if i in 'aeiou':
            b+=1
        else:
            c+=1
#main
a=input("a=")
word(a)
print(b)
print(c)