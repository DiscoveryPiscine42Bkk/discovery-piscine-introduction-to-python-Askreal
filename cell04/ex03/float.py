#!/usr/bin/env python3

num1 = float(input("Give me a number: "))
num2 = int(num1)

print("This number is an integer.") if num1 == num2 else print("This number is a decimal.")