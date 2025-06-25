#!/usr/bin/env python3
number = float(input("Give me a number: "))
if (int(number) == number):
    print(int(number))
else :
    rounded_up = int(number) + 1
    print(int(rounded_up))
