# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:12:40 2026

@author: User
"""
# Take input from the user # Program to find average marks and topper marks

# Taking number of students
# Program to calculate total bill from a list of product prices

# Number of products
n = int(input("Enter number of products: "))

prices = []

# Taking price input
for i in range(n):
    p = float(input(f"Enter price of product {i+1}: "))
    prices.append(p)

# Calculating total bill
total_bill = sum(prices)

print("\n--- BILL DETAILS ---")
print("Product Prices:", prices)
print("Total Bill =", total_bill)