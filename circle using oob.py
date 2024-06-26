# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:44:28 2023

@author: ramsa
"""

class cirle():
    __r=None
    __c=None
    def set(self):
        self.__r=int(input("enter the radius :"))
    def find(self):
        self.__c=3.14*self.__r**2
    def display(self):
        print(self.__c)
#main
a=cirle()
a.set()
a.find()
a.display()

        