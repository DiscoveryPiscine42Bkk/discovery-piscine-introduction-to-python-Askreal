#!/usr/bin/env python3
    
num = int(input("Enter a number less than \n"))
if (num >= 25):
    print(f'Error')
else :
    while num <= 25:
        print(f'Inside the loop, my variable is {num}')
        num += 1