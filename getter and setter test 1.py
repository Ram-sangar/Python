# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:42:11 2023

@author: ramsa
"""

class account:
    def __init__(self,balance,name):
       self.__balance = balance
       self.__name = name
    def credit(self,deposit):
       self.__balance = self.__balance + deposit
    def debit(self,withdrawal):
       self.__balance = self.__balance - withdrawal
    def get_name(self):
        return self.__name
    def get_balance(self):
        return self.__balance
    def set_name(self,name):
        self.__name = name
    def set_balance(self,balance):
            self.__balance = balance
#main
customer=account(0, "cyril")
print(customer.get_name())
print(customer.get_balance()) 
customer.credit(1000)
print(customer.get_name())
print(customer.get_balance()) 
customer.debit(500)
print(customer.get_name())
print(customer.get_balance()) 
customer.set_name("yogi") 
customer.credit(1000)
print(customer.get_name())
print(customer.get_balance()) 
customer.set_balance(500)
print(customer.get_name())
print(customer.get_balance()) 
        
        