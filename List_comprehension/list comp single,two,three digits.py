# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:16:10 2022

@author: ramsa
"""

import random as rd
b=[]
c=[]
d=[]
a=[rd.randint (0,1000) for i in range(0,100)]
b.append(a)
c.append(a)
d.append(a)
b=[i for i in a if(i<10)]
print('single digit',b)
c=[i for i in a if(i>9 and i<100)]
print('two digit',c)
d=[i for i in a if (i>100 and i<1000)]
print('three digit',d)
