# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:54:29 2023

@author: ramsa
"""
import random as rd
import pickle 
f=open("harish1.dat",'wb')
n=int(input("n="))
n=[rd.randint(-1000,1000) for i in range (n)]
pickle.dump(n,f)
f.close()
