# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:21:39 2023

@author: ramsa
program error
"""

import pickle 
f=open("harish1.dat",'rb')
a=open("single.dat",'wb')
b=open("twodigit.dat",'wb')
c=open("threedigit.dat",'wb')
d=open("fourdigit.dat","wb")
e=[]
f=[]
g=[]
h=[]
n=pickle.load(f)
for i in n:
    if (i>=0 and i<10) or (i>-10 and i<0):
       e.append(i)
    elif(i>9 and i<100) or (i>-100 and i<-9):
       f.append(i)
    elif(i>99 and i<1000) or (i>-1000 and i<-99):
       g.append(i)
    else:
       h.append(i)
pickle.dump(e,a)
pickle.dump(f,b)
pickle.dump(g,b)
pickle.dump(h,b)
f.close()