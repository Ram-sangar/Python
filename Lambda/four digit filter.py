# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:32:18 2023

@author: ramsa
"""

import random as rd
n=int(input("n="))
a=[rd.randint(0,10000) for i in range(n)]
b=filter(lambda x:x>999 and x<10000,a)
print(list(b))