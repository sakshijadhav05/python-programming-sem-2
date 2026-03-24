# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:05:54 2026

@author:sakshi jadhav 
"""
# Store expenses
file = open("expenses.txt", "a")

n = int(input("Enter number of days: "))
for i in range(n):
    amt = float(input(f"Enter expense for day {i+1}: "))
    file.write(str(amt) + "\n")

file.close()

# Calculate total
file = open("expenses.txt", "r")
total = 0

for line in file:
    total += float(line.strip())

file.close()

print("Total Monthly Expense =", total)