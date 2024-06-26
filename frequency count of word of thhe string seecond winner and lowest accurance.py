# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 10:31:12 2022

@author: ramsa
"""

s=input("s=")
l=s.split()
a=list(l)
b=set(a)
dic={}
for i in b:
    d=a.count(i)
    dic[i]=d
print(dic)
f=c=0
e=20
for i in dic:
    if f<dic[i]:
        f=dic[i]
        x=i
    elif e>dic[i]:
        e=dic[i]
        y=i
    if c<dic[i] and c!=f:
        c=dic[i]
        z=i
print("the highest key is:",x)  
print("the secound highest key is:",z)   
print("the lowest key is:",y) 
print("the highest frequency is:",f)  
print("the secound highest frequency is:",c) 
print("the lowest frequency is:",e) 

