# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:00:56 2022

@author: ramsa
"""

import random as rd
b=[]
c=[]
a=[rd.randint (-100,100) for i in range(0,100)]
b.append(a)
c.append(a)
b=[i for i in a if(i>0)]
print('positive',b)
c=[i for i in a if(i<0)]
print('negative',c)
