# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:19:47 2023

@author: ramsa
"""

import random as rd
n=int(input("n="))
y=[rd.randint(0,1000) for i in range (n)]
z=filter(lambda x:x<10,y)
print(list(z))
