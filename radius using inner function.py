# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 10:47:15 2023

@author: ramsa
"""

def circle(r):
    def area():
        return(3.14*r**2)
    def perimeter():
        return(2*3.14*r)
    print(area())
    print(perimeter())
#main
circle(10)