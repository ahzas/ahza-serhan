# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 10:37:32 2025

@author: AIRI
"""

print("Welcome to calculator")

value1 = float(input("Enter a value: "))

value2 = float(input("Enter a value: "))

process1 = value1+value2
process2 = value1*value2
process3 = value1-value2
process4 = value1/value2

choice = input("Select the action you want to take: ")

if choice == "+":
    print(f'{value1} + {value2} = {process1}')
    
elif choice == "*":
    print(process2)

elif choice == "-":
    print(process3)

elif choice == "/":
    print(process4)
    
else:
    print("You entered the wrong process!")
    

