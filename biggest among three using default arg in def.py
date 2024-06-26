# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:45:55 2022

@author: ramsa
"""
def big(a=20,b=100,c=150):
    h=a if a>c else c if a>c else b if b>c else c;
    return(h)
#main
x=big()
y=big(2000)
z=big(4000,3999,4000)
print(x,y,z)
