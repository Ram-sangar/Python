# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:43:02 2023

@author: ramsa
"""

num=int(input("a="))
sum=0
n1=len(str(num))
print(n1,"len")
temp=num
while temp>0:
    d=temp%10
    sum+=d**n1
    temp//=10
print(sum,"final")
