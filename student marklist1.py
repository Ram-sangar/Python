# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:17:36 2023

@author: ramsa
"""

import csv
f=open("STR.csv")
x=csv.reader(f)
a=["python","Asp.net","Compiler Design","Computer Networking","Java"]
c=[]
h=next(x)

for i in x:
    print("*********Student mark Statement*********")
    print(" ST.JOSEPH'S COLLEGE,(AUTONOMOUS),TRICHY ")
    print("---------Information Techonology---------")
    for j in range (0,5):    
        print(h[j],":",i[j],end="   ,   ")
    for j in range (0,5): 
        
        print(a[j],":",i[j+5])
    total=0
    for k in range (5,10):
         
         total+=(int(i[k]))
         avg=total/5
         if(int(i[k])>45):
             print(a[k-5],": pass")
         else:
             print(a[k-5],": fail")
    print("total",total)
    print("average",avg)
    

        
f.close()         
  
