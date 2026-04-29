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

def calculate_emi(principal, annual_rate, years):
    # Convert annual rate to monthly and years to months
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12

    # EMI formula
    emi = (principal * monthly_rate * (1 + monthly_rate)*months) / ((1 + monthly_rate)*months - 1)
    return emi

# Taking user input
p = float(input("Enter loan amount: "))
r = float(input("Enter annual interest rate (%): "))
t = int(input("Enter loan period (years): "))

emi_amount = calculate_emi(p, r, t)
print(f"\nEMI per month: ₹{emi_amount:.2f}")