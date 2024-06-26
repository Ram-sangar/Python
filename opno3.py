# -*- coding: utf-8 -*-
"""
Created on Sun May 14 19:16:59 2023

@author: ramsa
"""

from A3nos_accessing_3_values_using_inheritance import A3nos
class opno3(A3nos):
    def __init__(self,x=1000,y=500,z=700):
        A3nos.__init__(self,x,y) 
        A3nos.__init__(self,z)
    def sum(self):
        return self.getx() + self.gety() + self.getz()
    def product(self):
        return self.getx() * self.gety() * self.getz()
    def big(self):
        return ((self.getx() if self.getx() > self.getz() else self.getz()) if self.getx() > self.gety() else (self.gety() if self.gety() > self.getz() else self.getz()))
    def small(self):
        return ((self.getx() if self.getx() < self.getz() else self.getz()) if self.getx() < self.gety() else (self.gety() if self.gety() < self.getz() else self.getz()))
#main
a=opno3()
print(a.sum())
print(a.product())
print(a.big())
print(a.small())