# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:30:07 2023

@author: ramsa
"""

class sum():
    __a=None
    __b=None
    __c=None
    def __init__(self,a=300,b=400):
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
y=sum()
y.find()
y.display()
z=sum(10000,75000)
z.find()
z.display()
