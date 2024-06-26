# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 12:15:12 2022

@author: ramsa
"""


def big (*a):
    c=0
    for i in a:
        if i>c:
            c=i
    return(c)
b=big(1000,200,432,541,644,43244,35654,32454,735662,213)
print(b)
z=big(1,2,3,4,5,6,7,8,9,0)
print(z)