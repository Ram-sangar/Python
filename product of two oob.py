# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:38:39 2023

@author: ramsa
"""

class product():
    __a=None
    __b=None
    __c=None
    def set(self):
        self.__a=200
        self.__b=300
    def find(self):
        self.__c=self.__a*self.__b
    def display(self):
        print(self.__c)
#main
z=product()
z.set()
z.find()
z.display()