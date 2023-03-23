# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:20:14 2023

@author: USER
"""

print(list(range(10)))
print(list(range(1,10)))
print(list(range(2,10,2)))


num = int(input("次數:"))

total=0
for W in range(num): 
    print(W)
    total += W
print("總和:", total)

num = int(input("輸入階層:"))

total=1
for W in range(1,num+1): 
    print(W)
    total *= W
print("總和:", total)