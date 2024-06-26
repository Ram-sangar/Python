# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:56:44 2023

@author: ramsa
"""

class cirle():
    __r=None
    __c=None
    def __init__(self,r):
        self.__r=r
    def find(self):
        self.__c=3.14*self.__r**2
    def display(self):
        print(self.__c)
#main
a=cirle(20)
a.find()
a.display()