# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 11:41:53 2023

@author: ramsa
"""
import pickle
f=open("harish1.dat",'rb')
n=pickle.load(f)
a=0
b=0
c=0
d=0
a1=0
b1=0
c1=0
d1=0
for i in n:
    if i>=0 and i<10:
        a+=1
    elif i>-10 and i<0:
        a1+=1
    elif i>9 and i<100:
        b+=1
    elif i>-100 and i<-9:
        b1+=1
    elif i>99 and i<1000:
        c+=1
    elif i>-1000 and i<-99:
        c1+=1
    elif i==1000:
        d+=1
    elif i==-1000:
        d1+=1
print("positive single digit:",a,"Negative single digit:",a1)
print("positive two digit:",b,"Negative two digit:",b1)
print("positive three digit:",c,"Negative three digit:",c1)
print("positive four digit:",d,"negative four digit:",d1)
f.close()
        