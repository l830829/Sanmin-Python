# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:55:14 2023

@author: USER
"""

import random
ans=random.randint(1,100)
guess=0
while guess != ans:
    guess=int(input("輸入1～100之間猜數:"))
    if guess > ans:
        print("猜小一點")
    elif guess < ans:
        print("猜大一點")
print("猜對了")

print()

import random
ans=random.randint(1,100)
print(random.random())


for i in range(1,100):
    if i == 20:
        break
    if i % 3 == 0:
        continue
    print(i)
    print("相乘之和:",i*i)