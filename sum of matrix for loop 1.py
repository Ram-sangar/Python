# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:30:25 2022

@author: ramsa
"""

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
        r=int(input('r='))
        q.append(r)
    p.append(q)   
x=[]
n=3
for i in range (n):
    y=[]
    for j in range (n):
        z=int(input('z='))
        y.append(z)
    x.append(y)  

f=[]
for i in range(n):
    e=[]
    for j in range (n):
        d=b[i][j]+p[i][j]+x[i][j]
        e.append(d)
    f.append(e)
for i in range (n):
    for j in range (n):
        print(f[i][j],end="")
    print()
