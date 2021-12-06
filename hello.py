#!/usr/bin/env python3

name = input("What is your name? ") 
age = int(input("What is your age? "))

if age <= 11:
    print(f"Hello {name}! You are a child")
elif age >= 12 and age <= 18:
    print(f"Hello {name}! You are a teen")
elif age >= 19 and age <= 65:
    print(f"Hello {name}! You are an adult ")

