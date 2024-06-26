# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:19:59 2023

@author: ramsa
"""

def word(a):
    b=0
    c=0
    l=len(a)
    for i in range(l):
        if(a[i]=='a' or a[i]=='e'or a[i]=='i'or a[i]=='o' or a[i]=='u'):
            b+=1
        else:
            c+=1
    return(b,c)
#main
a=input("a=")
b=word(a)
print(b)