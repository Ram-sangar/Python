# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:02:29 2023

@author: ramsa
"""

import csv
f=open("STR.csv")
x=csv.reader(f)
h=next(x)
for i in x:
    for j in range (0,10):
        print(h[j],":",i[j])
f.close()