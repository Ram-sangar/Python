# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 11:39:48 2023

@author: ramsa
"""

import random as rd
n=int(input("n="))
y=[rd.randint(-10,10) for i in range (n)]
z=filter (lambda x:x>0,y)
print(list(z))