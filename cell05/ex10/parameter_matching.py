#! /usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else :
    new_text = str(input("What was the parameter? "))
    if (new_text == sys.argv[1]):
        print("Good job!")
    else : print("Nope, sorry...")

