# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:24:34 2023

@author: ramsa
"""

import random as rd
def far(x):
    a=5/9*(x-32)
    return(a)
a=[rd.randint(100,120) for i in range(20)]
b=map(lambda x:far(x),a)
print(list(b))