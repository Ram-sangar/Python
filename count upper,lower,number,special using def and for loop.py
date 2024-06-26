# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:43:59 2023

@author: ramsa
"""

def word(a):
    b=c=d=e=0
    for i in a:
        if(i>="A"and i<="Z"):
            b+=1
        elif(i>="a"and i<="z"):
            c+=1
        elif(i>="0"and i<="9"):
            d+=1
        else:
            e+=1
    return(b,c,d,e)
#main
a=input("a=")
b=word(a)
print(b)