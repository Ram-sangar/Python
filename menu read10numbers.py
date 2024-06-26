# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:44:57 2023

@author: ramsa
"""

def menu():
    b=int(input("b="))
    return(b)
#main
c=menu()
while(c!=10):
    print(c)
    c=menu()