# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 12:12:51 2023

@author: ramsa
"""

a=b=c=d=0
def word(e):
    global a,b,c,d
    for i in e:
        if(i>="A" and i<="Z"):
            a+=1
        elif(i>='a' and i<='z'):
            b+=1
        elif(i>="0" and i<='9'):
            c+=1
        else:
            d+=1
#main
e=input("a=")
word(e)
print(a)
print(b)
print(c)
print(d)