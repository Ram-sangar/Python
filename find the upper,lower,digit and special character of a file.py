# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:17:32 2023

@author: ramsa
"""

f=open("cyril.txt")
n=m=p=q=0
for i in f:
    for j in i:
        a=ord(j)
        if a>=65 and a<=90:
            n+=1
        elif a>=97 and a<=122:
            m+=1
        elif a>=48 and a<57:
            p+=1
        else:
            q=+1
print("upper:",n)
print("Lower:",m)
print("digit:",p)
print("special character:",q)
f.close()