# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:26:18 2023

@author: ramsa
"""

class A2nos:
    __x=None
    __y=None
    def __init__(self,x=10,y=20):
        self.__x=x
        self.__y=y
    def setx (self,x):
        self.__x=x
    def sety (self,y):
        self.__y=y
    def setxy (self,x,y):
        self.__x=x
        self.__y=y
    def setb (self,b):
        self.__x=b.__x
        self.__y=b.__y
    def reset (self):
        self.__x=10
        self.__y=20
    def getx(self):
        return self.__x
    def gety (self):
        return(self.__y)
    def getxy (self):
        return(self.__x,self.__y)
    def print(self):
        print(self.__x,self.__y)
#main
a=A2nos()
b=A2nos(24,77)
a.print()      
a.setx(20)
print(a.getx())
a.sety(80)
print (a.gety())
a.setxy(100,200)
print(a.getxy())
a.reset()
a.print() 
a.setb(b)
a.print()
