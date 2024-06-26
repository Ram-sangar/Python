# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:23:03 2023

@author: ramsa
"""

def menu():
    b=int(input("b="))
    return(b)
def menu():
   print("1:pattern1")   
   print("2:pattern2")  
   print("3:pattern3")  
   print("4:pattern4")  
   print("5:pattern5")  
   print("6:pattern6")  
   print("7:pattern7")  
   print("8:pattern8")  
   print("9:pattern9")  
   print("10:exit")  
   b=int(input("b="))
   return(b)
def pattern1():
    for  i in range(1,6):
        print("*"*i)
    for i in range(4,0,-1):
        print("*"*i)
def pattern2():
    for  i in range(5,0,-1):
        print("*"*i)
    for i in range(2,6):
        print("*"*i)
def pattern3():
    n=6
    m=4
    for  i in range(1,n):
        print(" "*m, "*"*i)
        m-=1
    m=4
    for i in range(1,n-1):
        print(" "*i,"*"*m)
        m-=1
def pattern4():
    m=n=7

    for  i in range(0,n,1):
        print(" "*i, "*"*m)
        m-=1
    m=5
    for i in range(2,n+1):
        print(" "*m,"*"*i)
        m-=1
def pattern5():
    n=1
    for i in range(5,0,-1):
        print(" "*i,"*"*n)
        n+=2
def pattern6():
    n=1
    for i in range(4,-1,-1):
        print(" "*i,"*"*n)
        n+=2
    n=7
    for i in range(1,6):
        print(" "*i,"*"*n)
        n-=2  
def pattern7():
    print("*"*8)
    i=1
    while(i<5):
        print("*"*1," "*4,"*"*1)
        i+=1
    print("*"*8)

#main
c=menu()
while(c!=10):
    if(c==1):
        pattern1()
    elif(c==2):
        pattern2()
    elif(c==3):
        pattern3()
    elif(c==4):
        pattern4()
    elif(c==5):
         pattern5() 
    elif(c==6):
        pattern6()
    elif(c==7):
        pattern7()
    
    c=menu()