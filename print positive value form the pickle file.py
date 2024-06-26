# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:20:00 2023

@author: ramsa
"""

import pickle 
f=open("harish1.dat",'rb')
n=pickle.load(f)
for i in n:
    if (i>0):
        
       print("positive",i)
    
  
f.close()