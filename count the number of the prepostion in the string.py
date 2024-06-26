# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:46:03 2022

@author: ramsa
"""

s=input("s=")
a=s.split()
b=list(a)
c=set(b)
d=['a','the','an','is','that','they','then','were','was','should','has','had','have']
e=set(d)
print(b)
print(e)
for i in e:
    print(i)
    y=b.count(i)
    print(y)
