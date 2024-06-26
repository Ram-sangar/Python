# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:32:59 2023

@author: ramsa
"""

import random as rd
a=b=c=d=0
def digit(e):
    global a,b,c,d
    for i in e:
        if(i>=0 and i<=9):
            a+=1
        elif(i>=10 and i<=99):
            b+=1
        elif(i>=100 and i<=999):
            c+=1
        elif(i>=1000 and i<=9999):
            d+=1
        else:
            print("the value is above for 4 digit:",i)
#main
n=int(input("n="))
e=[rd.randint(0,9999) for i in range(n)]
digit(e)
print(a,"single digit")
print(b,"two digit")
print(c,"three digit")
print(d,"four digit")
