# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:49:26 2022

@author: ramsa
"""
def big(a=20,b=100,c=150):
    h=a if a>c else c if a>c else b if b>c else c;
    e=a if a<c else c if a<c else b if b<c else c;
    return(h,e)
#main
x=big(c=1000,b=500,a=200)
y=big(b=2000)
z=big(b=400,a=3999,c=4000)
print(x,y,z)
