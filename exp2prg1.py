# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:16:45 2026

@author: User
"""

year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0): 
  print("Leap Year")
else:
  print("Not a Leap Year")