# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 10:41:07 2023

@author: ramsa
"""

def fn(**x):
    for i in x:
        print(i,x[i])
#main
a=fn(name='cyril',age=25,salary=90000,place='trichy')
b=fn(name='dhil',age=20,salary=50000,place='chennai')