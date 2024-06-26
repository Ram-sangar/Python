# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:20:13 2022

@author: ramsa
"""

b=[]
n=3
for i in range (n):
    a=[]
    for j in range (n):
        c=int(input('c='))
        a.append(c)
    b.append(a)   

p=[]
n=3
for i in range (n):
    q=[]
    for j in range (n):
        r=int(input('c='))
        q.append(r)
    p.append(q)   

       print(b[i][j],end="")  for j in range (n):
   
x=[]
n=3
for i in range (n):
    y=[]
    for j in range (n):
        z=int(input('c='))
        y.append(z)
    x.append(y)  

f=[]
for  in range(n):
    e=[]
    for j in range (n):
        d=b[i][j]+p[i][j]+x[i][j]
        e.append(d)
    f.append(e)
for i in range (n):
    for j in range (n):
        print(f[i][j],end="")
        print()
