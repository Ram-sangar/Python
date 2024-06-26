# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:55:30 2023

@author: ramsa
"""

class circle:
    __r=None
    __c=None
    def __init__(self,r=10):
        self.__r=r
    def cir(self):
        self.__c = 3.14 * self.__r ** 2
    def setr(self,r):
        self.__r=r
    def reset(self):
        self.__r=10
    def getr(self):
        return self.__r
    def getc(self):
        return self.__c
    def getall(self):
        return(self.__r,self.__c)
    def print(self):
        print(self.__r,self.__c)

#main
a=circle()
a.cir()
print(a.getr())
print(a.getc())
a.setr(200)
a.cir()
print(a.getr())
print(a.getc())
print(a.getall())
a.reset()
a.cir()
a.print()

        
        