# -*- coding: utf-8 -*-
"""
Created on Sun May 14 09:53:44 2023

@author: ramsa
"""

from accessing import A2nos
class op2nos(A2nos):
  
    def __init__(self,x=1000,y=200):
    
        A2nos.__init__(self,x,y)
        
    def sum (self):
        print("X :",self.getx())
        print("Y :",self.gety())
        return (self.getx() + self.gety())
    def diff (self):
        return (self.getx() - self.gety())
    def mul (self):
        print("X :",self.getx())
        print("Y :",self.gety())
        return (self.getx() * self.gety())
    def mod (self):
        return (self.getx() % 13)
    def quo (self):
        return (self.getx() / self.gety())
    def floor(self):
        return (self.getx() // self.gety())
    def exp(self):
        return (self.getx() ** 2)
    
#main
z=op2nos()
print("sum :",z.sum())
print("diff :",z.diff())
print("mul :",z.mul())
print("mod :",z.mod())
print("quo :",z.quo())
print("floor :",z.floor())
print("exp :",z.exp())