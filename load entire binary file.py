# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:43:27 2023

@author: ramsa
"""

import pickle
f=open("harish1.dat","rb")
n=pickle.load(f)
print(n)
f.close()