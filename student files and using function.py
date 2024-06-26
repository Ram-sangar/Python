# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 12:20:32 2023

@author: ramsa
"""

import csv
f=open("str.csv")
x=csv.reader(f)
h=next(x)
def menu():
    print("1:CIA MARKLIST")
    print("2:INDIVIDUAL MARKLIST")
    a=int(input("enter the number:"))
    return(a)
def cia():
    print("1:PYTHON")
    print("2:ASP.NET")
    print("3:COMPILER DESIGN")
    print("4:COMPUTER NETWORKS")
    print("5:JAVA")
    b=int(input("enter the number:"))
    return(b)
def python():
    print("st.joseph's college(Autonomous),Trichy")
    print("Department of IT")
    
    for i in x:
            
             if(int(i[5])>=45):
                 print(h[0],":",i[0],h[1],':',i[1],h[2],":",i[2],h[5],":",i[5],"pass")
             else:
                 print(h[0],":",i[0],h[1],':',i[1],h[2],":",i[2],h[5],":",i[5],"fail")
c=menu()
while(c!=3):
    if(c==1):
        d=cia()
        while(d!=6):
            if(d==1):
                python()
f.close()

            
            