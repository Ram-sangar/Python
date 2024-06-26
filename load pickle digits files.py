# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:30:29 2023

@author: ramsa
"""

import pickle
a=input("a=")
f=open(a,"rb")
n=pickle.load(f)
print(n)
f.close()
