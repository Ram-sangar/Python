# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 10:54:34 2022

@author: ramsa
"""

a=[i for i in range(0,101) if not (i%3==0 or i%5==0 or i%7==0)]
print(a)