# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:16:45 2026

@author: User
"""

# Traffic Police Speed Check

# Movie Ticket Eligibility Check

# Loan Approval System

# Receipt Copy Printer using Nested Loops

# Multiplication tables from 1 to 10

def simple_interest(principal, rate, time): 
  si = (principal * rate * time) / 100 
  return si
# Taking input from the user
p = float(input("Enter principal amount: ")) 
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): ")) 
# Function call
interest = simple_interest(p, r, t) 
print("Simple Interest is:", interest)