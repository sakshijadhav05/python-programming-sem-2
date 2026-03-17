# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 07:12:17 2026

@author: sakshi jadhav 
"""

# Creating an empty dictionary
student = {}
# Adding key-value pairs
student["name"] = "Rahul"
student["age"] = 20
student["course"] = "Python"
print("Dictionary after adding elements:")
print(student)
# Updating a value
student["age"] = 21
print("\nDictionary after updating a value:")
print(student)
# Deleting a key-value pair
del student["course"]
print("\nDictionary after deleting a key-value pair:")
print(student)