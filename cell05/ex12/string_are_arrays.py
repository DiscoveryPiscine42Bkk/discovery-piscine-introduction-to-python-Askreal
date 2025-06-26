#!/usr/bin/env python3
import sys
import re

if len(sys.argv or 'z' not in sys.argv[1]) != 2:
    print(f'none')
else :
    text = sys.argv[1]
    print(f'z'*len(re.findall('z' , text)))    

    print(re.findall('z' , text))
    print(len(re.findall('z' , text)))
print(sys.argv)