# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:32:11 2023

@author: USER
"""

for i in range(1,6):
    for y in range(1,i):
        print(y,end="")
    print()

print()

for i in range(1,6):
    for y in range(0,i):
        print(i,end="")
    print()
    
print()

for i in range(1,6):
    for y in range(1,i+1):
        print(i,end="")
    print()