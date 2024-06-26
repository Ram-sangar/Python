# -*- coding: utf-8 -*-
"""
Created on Sat May 13 19:16:57 2023

@author: ramsa
"""

from accessing import A2nos
class point(A2nos):
      pass
#main
c=point()
c.print()
c.setx(20)
print(c.getx())
c.sety(40)
print(c.gety())
b=point(50)
c.setb(b)
print(c.getall())
