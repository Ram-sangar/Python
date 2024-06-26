# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:18:35 2023

@author: ramsa
"""
import pickle 
f=open("harish1.dat",'rb')
n=pickle.load(f)
for i in n:
    print(i)
f.close()
