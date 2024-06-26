# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:34:07 2023

@author: ramsa
"""

class cirle():
    __r=None
    __c=None
    def __init__(self,r=30):
        self.__r=r
    def find(self):
        self.__c=3.14*self.__r**2
    def display(self):
        print(self.__c)
#main
a=cirle(20)
a.find()
a.display()
b=cirle()
b.find()
b.display()