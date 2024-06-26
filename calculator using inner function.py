# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 10:59:41 2023

@author: ramsa
"""

def cal(a,b,opr):
    def sum():
        return(a+b)
    def minus():
        return(a-b)
    def mul():
        return(a*b)
    def div():
        return(a/b)
    if(opr=="+"):
        print(sum())
    elif(opr=="-"):
        print(minus())
    elif(opr=="*"):
        print(mul())
    elif(opr=="/"):
        print(div())
#main
cal(10,20,"*")
cal(70,35,"-")
cal(80,2,"+")
cal(102,4,"/")