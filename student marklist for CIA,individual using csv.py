# -*- coding: utf-8 -*-
"""
Created on Thu May 11 09:52:29 2023

@author: ramsa
"""

import csv
f=open ("STR.csv")
x=csv.reader(f)
h=next(x)
def menu():
    print("1:CIA MARK")
    print("2:INDIVIDUAL MARKLIST")
    print("3:EXIT")
    a=int(input("enter a number :"))
    return(a)

def CIA():
    print("4:PYTHON CIA")
    print("5:ASP.NET CIA")
    print("6:COMPILER DESIGN CIA")
    print("7:COMPUTER NETWORK CIA")
    print("8:JAVA")
    print("9:EXIT")
    b=int(input("enter a number:"))
    return(b)

def Python():
   
    for i in x:
        print(" ")
        print("                                  Student CIA Python                        ")
        print("                    St.Joseph's College,(Autonomous),Trichy-02             ")
        print("                                  Department Of IT                         ")
        if(int(i[5])>=45):
            print("        ",h[0],":",i[0],",",h[1],":",i[1],",",h[2],":",i[2],",",h[5],":",i[5],",","pass")
        else:
            print("        ",h[0],":",i[0],",",h[1],":",i[1],",",h[2],":",i[2],",",h[5],":",i[5],",","Fail")   
        

def Asp():
    
    for i in x:
        print(" ")
        print("                                   Student CIA Asp                         ")
        print("                    St.Joseph's College,(Autonomous),Trichy-02             ")
        print("                                  Department Of IT                         ")
        if(int(i[6])>=45):
            print("        ",h[0],":",i[0],",",h[1],":",i[1],",",h[2],":",i[2],",",h[6],":",i[6],",","pass")
        else:
            print("        ",h[0],":",i[0],",",h[1],":",i[1],",",h[2],":",i[2],",",h[6],":",i[6],",","Fail")
            
def Compiler_Design():
   
    for i in x:
        print(" ")
        print("                              Student CIA Compiler Design                  ")
        print("                    St.Joseph's College,(Autonomous),Trichy-02             ")
        print("                                  Department Of IT                         ")
        if(int(i[7])>=45):
            print("        ",h[0],":",i[0],",",h[1],":",i[1],",",h[2],":",i[2],",",h[7],":",i[7],",","pass")
        else:
            print("        ",h[0],":",i[0],",",h[1],":",i[1],",",h[2],":",i[2],",",h[7],":",i[7],",","Fail")
            
def Computer_Network():
    
    for i in x:
        print(" ")
        print("                              Student CIA Computer Network                 ")
        print("                    St.Joseph's College,(Autonomous),Trichy-02             ")
        print("                                  Department Of IT                         ")
        if(int(i[8])>=45):
            print("        ",h[0],":",i[0],",",h[1],":",i[1],",",h[2],":",i[2],",",h[8],":",i[8],",","pass")
        else:
            print("        ",h[0],":",i[0],",",h[1],":",i[1],",",h[2],":",i[2],",",h[8],":",i[8],",","Fail")
            
def Java():
    
    for i in x:
        print(" ")
        print("                                  Student CIA Java                            ")
        print("                    St.Joseph's College,(Autonomous),Trichy-02             ")
        print("                                  Department Of IT                         ")
        if(int(i[9])>=45):
            print("        ",h[0],":",i[0],",",h[1],":",i[1],",",h[2],":",i[2],",",h[9],":",i[9],",","pass")
        else:
            print("        ",h[0],":",i[0],",",h[1],":",i[1],",",h[2],":",i[2],",",h[9],":",i[9],",","Fail")
          
def Individual():
    for i in x:
        print("                                  Student Marklist                         ")
        print("                    St.Joseph's College,(Autonomous),Trichy-02             ")
        print("                                  Department Of IT                         ")
        for j in range (0,5):
            print(h[j],":",i[j],end="    ")
        total=0
        for k in range (5,10):
            total+=(int(i[k]))
            avg=total/5
            if(int(i[k])>45):
                print(h[k],":",i[k],":Pass")
            else:
                print(h[k],":",i[k],":Fail")
        print("Total :",total)
        print("Average :",avg)
        print("                                           ")
      
#main
c=menu()
while(c!=3):
    if(c==1):
        d=CIA()
        while(d!=9):
        
            if(d==4):
                Python()
            elif(d==5):
                Asp()
            elif(d==6):
                Compiler_Design()
            elif(d==7):
                Computer_Network()
            elif(d==8):
                Java()
            d=CIA()
            f.seek(0)
            h=next(x)
    elif(c==2):
        Individual()
    
    c=menu()
f.close()
                