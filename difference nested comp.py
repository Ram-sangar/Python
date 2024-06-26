# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 09:56:06 2022

@author: ramsa
"""

n=3
a=[[int(input()) for j in range (n)]for i in range(n)]
b=[[int(input()) for j in range (n)]for i in range(n)]
c=[[a[i][j]-b[i][j] for j in range (n)]for i in range(n)]
print(c)