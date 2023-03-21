# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:41:40 2023

@author: iant
"""

def login(name="guest"):
    print("welcome,",name)
    fun("name",123)
    add(10,20)
login("snehal")
#-------keyword argument-----
def fun(name,id):
    print(name,id)
#-------Arbitary argument------
def add(*no):
    sum=0
    for n in no:
        sum=sum+n;
        print("total",sum)