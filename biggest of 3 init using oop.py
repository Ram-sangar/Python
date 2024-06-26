# -*- coding: utf-8 -*-
"""
Created on Thu May 11 19:35:08 2023

@author: ramsa
"""

class big_3():
    __a=None
    __b=None
    __c=None
    __d=None
    def __init__(self):
        self.__a=int(input("enter the a value :"))
        self.__b=int(input("enter the b value :"))
        self.__c=int(input("enter the c value :"))
    def find(self):
        self.__d=(self.__a if self.__a>self.__c else self.__c)if self.__a>self.__b else (self.__b if self.__b>self.__c else self.__c)
    def display(self):
        print(self.__d)
#main
e=big_3()
e.find()
e.display()