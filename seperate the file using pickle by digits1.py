# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:25:23 2023

@author: ramsa
"""

import pickle 
f=open("harish1.dat",'rb')
b=open("positive.dat",'wb')
z=open("singledigit.dat",'wb')
c=open("twodigit.dat",'wb')
e=open("threedigit.dat",'wb')
v=open("fourdigit.dat","wb")
n=pickle.load(f)
a=[]
d=[]
g=[]
y=[]
x=[]
for i in n:
    if (i>0):
        a.append(i)
    elif (i>=0 and i<10) or (i>-10 and i<0):
       y.append(i)
    elif(i>9 and i<100) or (i>-100 and i<-9):
       d.append(i)
    elif(i>99 and i<1000) or (i>-1000 and i<-99):
       g.append(i)
    elif (i==1000) or (i==-1000):
        x.append(i)
    

pickle.dump(a,b)  
pickle.dump(d,c) 
pickle.dump(g,e)
pickle.dump(y,z)
pickle.dump(x,v)
f.close()
b.close()
c.close()
e.close()
z.close()
v.close()