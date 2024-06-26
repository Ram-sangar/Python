# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:29:16 2023

@author: ramsa
"""

class big_3():
    __a=None
    __b=None
    __c=None
    __d=None
    def __init__(self,a=1,b=3,c=2):
        self.__a=a
        self.__b=b
        self.__c=c
    def find(self):
        self.__d=(self.__a if self.__a>self.__c else self.__c)if self.__a>self.__b else (self.__b if self.__b>self.__c else self.__c)
    def display(self):
        print(self.__d)
#main
e=big_3(1000,2003,2000)
e.find()
e.display()
f=big_3()
f.find()
f.display()
g=big_3(c=1000)
g.find()
g.display()