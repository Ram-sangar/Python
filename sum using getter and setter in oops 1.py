# -*- coding: utf-8 -*-
"""
Created on Sat May 13 10:37:35 2023

@author: ramsa
"""

class sum:
    __x=None
    __y=None
    __s=None
    def __init__(self,x=40,y=50):
        self.__x=x
        self.__y=y
    def setx(self,x):
        self.__x=x
    def sety(self,y):
        self.__y=y
    def setxy(self,x,y):
        self.__x=x
        self.__y=y
    def sum(self):
        self.__s=self.__x+self.__y
    def reset(self):
        self.__x=40
        self.__y=50
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def gets(self):
        return self.__s #self.sets()
    def getall(self):
        return self.__x,self.__y,self.__s 
    def print(self):
        print(self.__x,self.__y,self.__s)
#main
a=sum()
a.sum()
print(a.getx())
print(a.gety())
print(a.gets())
print(a.getall())
a.setx(400)
a.sum()
a.print()
a.sety(500)
a.sum()
a.print()
a.setxy(1000,500)
a.sum()
a.print()
a.reset()
a.sum()
a.print()
