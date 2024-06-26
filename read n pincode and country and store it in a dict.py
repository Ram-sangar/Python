# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:50:54 2022

@author: ramsa
"""

n=int(input('n='))
dic={}
for i in range (n):
    pincode=int(input("pincode="))
    country=input("country=")
    dic[pincode]=country
print(dic)