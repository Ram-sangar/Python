# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 10:41:07 2023

@author: ramsa
"""


def num (*c):
    a=0
    b=9999
    for i in c:
        if i>a:
            a=i
        if b>i:
            b=i
    return(a,b)
#main
d=num(100,500,250,400,1000,115,180,222,500)
e=num(112,134,133,182,191,106,129,194,198)
print(d)
print(e)
            
        
            