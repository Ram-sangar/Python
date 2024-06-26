# -*- coding: utf-8 -*-
"""
Created on Thu May 11 19:19:52 2023

@author: ramsa
"""

class sum():
    __a=None
    __b=None
    __c=None
    def __init__(self):
        self.__a=10
        self.__b=20
    def find(self):
        self.__c=self.__a + self.__b
    def display(self):
        print(self.__c)
#main
x=sum()
x.find()
x.display()

"""

class sum():
    __a=None
    __b=None
    __c=None
    def set(self):
        self.__a=10
        self.__b=20
    def find(self):
        self.__c=self.__a + self.__b
    def display(self):
        print(self.__c)
#main
x=sum()
x.set()
x.find()
x.display()

"""