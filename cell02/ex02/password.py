#!/usr/bin/env python3
correct_password = "Python is awesome"

password = str(input()) 
print("ACCESS GRANTED") if correct_password == password else print("ACCESS DENIED")

