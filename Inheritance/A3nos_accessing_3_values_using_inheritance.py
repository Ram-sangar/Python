# -*- coding: utf-8 -*-
"""
Created on Sun May 14 11:54:33 2023

@author: ramsa
"""

from accessing import A2nos
class A3nos(A2nos):
    def __init__(self,x=50,y=45,z=30):
        self.__z=z
        A2nos.__init__(self,x,y)
        
    def set3 (self,z):
            self.__z=z
    def setxy3 (self,x,y,z):
            A2nos.setxy(self,x,y)
            self.__z=z
    def reset (self):
            A2nos.reset(self)
            self.__z=30
            
    def setb (self,b):
            A2nos.setb(self,b)
            self.__z=b.__z
    def getz(self):
            return self.__z
    def getxy3(self):
            return A2nos.getxy(self),self.__z
    def print3(self):
            print(self.__z)
    def printall(self):
            print(A2nos.getxy(self),self.__z)
#main
a=A3nos()

a.set3(130)
print(a.getz())
a.setxy3(145,175,178)
print(a.getxy3())
a.reset()
a.printall()

b=A3nos(56,43,25)
a.setb(b)
a.printall()
            