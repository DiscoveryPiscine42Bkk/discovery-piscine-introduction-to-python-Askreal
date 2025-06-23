#!/usr/bin/env python3

text = str(input())
new_text = ""
for i in text:
    if (i.isupper()):
        new_text += i.lower()
    else : 
        new_text += i.upper()
print(new_text)