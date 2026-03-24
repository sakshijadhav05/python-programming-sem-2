# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:22:57 2026

@author: sakshi jadhav
"""
file = open("report.txt", "r")

text = file.read()
words = text.split()

print("Total number of words =", len(words))

file.close()