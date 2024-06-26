# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:09:16 2023

@author: ramsa
"""

import csv
f=open("STR.csv")
x=csv.reader(f)
h=next(x)
print(h)
for i in x:
    print(i)
f.close()