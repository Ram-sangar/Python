# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:50:38 2023

@author: ramsa
"""

import csv
f=open("STR.csv")
x=csv.reader(f)
for i in x:
    print(i)
f.close()