# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:16:45 2026

@author: User
"""

n = int(input("Enter number:")) 
fact = 1
for i in range(1, n + 1): 
   fact = fact * i
print("Factorial:", fact)