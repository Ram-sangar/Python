# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:50:06 2023

@author: ramsa
"""
class sum:
    __x=None
    __y=None
    __s=None
    def __init__(self):
        self.reset()
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def set_x(self,x):
        self.__x = x
    def set_y(self,y):
        self.__y = y
    def set_xy(self,x,y):
        self.__x=x
        self.__y=y
    def find(self):
        self.get_s()
    def get_s(self):
        self.__s=self.__x + self.__y
    def display(self):
        print(self.__s)
    def reset(self):
        self.__x = 10
        self.__y = 20
        
#main
z=sum()
print(z.get_x())
print(z.get_y())
z.set_x(1000)
z.set_y(300)
z.set_xy(10000,5000)
print(z.get_x())
print(z.get_y())
z.find()
z.display()
 
    