# -*- coding: utf-8 -*-
"""
Created on Thu May 11 19:22:00 2023

@author: ramsa
"""

class product():
    __a=None
    __b=None
    __c=None
    def __init__(self):
        self.__a=200
        self.__b=300
    def find(self):
        self.__c=self.__a*self.__b
    def display(self):
        print(self.__c)
#main
z=product()
z.find()
z.display()