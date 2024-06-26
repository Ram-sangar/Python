# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:19:55 2022

@author: ramsa
"""

def big(a=20,b=100,c=150):
    h=a if a>c else c if a>c else b if b>c else c;
    return(h)
#main
x=big()
y=big(b=2000)
z=big(c=4000,b=3999,a=4000)
print(x,y,z)