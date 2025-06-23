#!/usr/bin/env python3
import sys

if len(sys.argv) == 0:
    i = 0
    j = 0

    while i <= 10:
        print(f"Table de {i}: ", end="")
        while j <= 10 :
            print(f" {i*j} " , end = "")
            j += 1
        print("\n")
        j = 0
        i +=1
else : print("None")