# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:03:49 2022

@author: ramsa
"""

n=3
a=[[int(input())for j in range (n)]for i in range (n)]
b=[[int(input())for j in range (n)]for i in range (n)]
c=[[a[i][j]+b[i][j]for j in range (n)]for i in range (n)]
print(c)