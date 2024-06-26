# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:47:54 2023

@author: ramsa
"""

class sum():
    __a=None
    __b=None
    __c=None
    def __init__(self,a,b):
        self.__a=a
        self.__b=b
    def find(self):
          self.__c=self.__a + self.__b
    def display(self):
           print(self.__c)
#main
x=sum(10,20)
x.find()
x.display()