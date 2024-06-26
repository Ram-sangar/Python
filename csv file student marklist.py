# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:41:46 2023

@author: ramsa
"""

import csv
f=open("STR.csv")
x=csv.reader(f)
h=next(x)
for i in x:
    print("*********Student mark Statement*********")
    print(" ST.JOSEPH'S COLLEGE,(AUTONOMOUS),TRICHY ")
    print("---------Information Techonology---------")
    for j in range (0,5):    
        print(h[j],":",i[j],end="   ")
    total=0   
    for k in range (5,10):
             
             total+=(int(i[k]))
             avg=total/5
             if(int(i[k])>=45):
                 print(h[k]," : ",i[k]," : pass")
             else:
                 print(h[k]," : ",i[k]," : fail")
    print("Total",total)
    print("average",avg)
    print("#########################################")
f.close()
