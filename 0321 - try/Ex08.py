# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:55:14 2023

@author: USER
"""

ans=91
guess=0
while guess != ans:
    guess=int(input("輸入1～100之間猜數:"))
    if guess > ans:
        print("猜小一點")
    elif guess < ans:
        print("猜大一點")
print("猜對了")