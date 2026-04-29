# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:16:45 2026

@author: User
"""

# Traffic Police Speed Check

# Movie Ticket Eligibility Check

# Loan Approval System

# Receipt Copy Printer using Nested Loops

copies = int(input("Enter number of receipt copies: "))
items = int(input("Enter number of items: "))

for i in range(1, copies + 1):
    print(f"\nReceipt Copy {i}:")
    for j in range(1, items + 1):
        print(f"Item Number: {j}")