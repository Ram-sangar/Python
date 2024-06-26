# -*- coding: utf-8 -*-
"""
Created on Sat May 13 12:16:24 2023

@author: ramsa
"""

class big:
    __a=None
    __b=None
    __c=None
    __d=None
    def __init__(self,a=70,b=30,c=50):
        self.__a=a
        self.__b=b
        self.__c=c
    def big1(self):
        self.__d = (self.__a if self.__a >self.__c else self.__c) if self.__a > self.__b else (self.__b if self.__b >self.__c else self.__c) 
    def seta(self,a):
        self.__a=a
    def setb(self,b):
        self.__b=b
    def setc(self,c):
        self.__c=c
    def setabc(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def reset (self):
        self.__a=70
        self.__b=30
        self.__c=50
    def geta (self):
        return self.__a
    def getb (self):
        return self.__b
    def getc (self):
        return self.__c
    def getd (self):
        return self.__d 
    def getall (self):
        return self.__a,self.__b,self.__c,self.__d 
    def print(self):
        print(self.__a,self.__b,self.__c,self.__d)
        
#main
a=big()
a.big1()
a.print()
a.seta(150)
a.big1()
a.print()
a.setb(500)
a.big1()
print(a.getb())
a.print()
a.setc(200)
a.big1()
a.print()
a.setabc(1000,1001,1003)
a.big1()
a.print()
