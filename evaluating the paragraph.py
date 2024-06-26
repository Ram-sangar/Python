# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 10:10:01 2022

@author: ramsa
"""

s=input("s=")
k={'communication','logical',' problems','machine',' code','fast','quick ','to search ','the ','information','graphical','design','analysis the data','game design','web design','i12th generation'}
l=s.split()
a=list(l)
b=k.intersection(a)
c=len(b)
if c>=10:
    print('you mark is:',c,"your o grade excellent")
elif c>=7 or c>=9:
    print('you mark is:',c,'your A grade very good')
elif c>=4 or c>=6:
    print('you mark is:',c,'your B grade good')
elif c<4:
    print('you mark is:',c,'your are fail try again')    
