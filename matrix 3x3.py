# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:40:00 2023

@author: ramsa
"""

b=[]
n=3
i=0
while i<n:
    a=[]
    j=0
    while j<n:
        d=int(input("d="))
        a.append(d)
        j=j+1
    b.append(a)
    i=i+1
i=0
while i<n:
    j=0
    while j<n:
      print(b[j][i],end='')
      j=j+1
    i=i+1
    print()