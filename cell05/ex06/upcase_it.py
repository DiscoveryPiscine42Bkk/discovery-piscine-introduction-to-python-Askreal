#!/usr/bin/env python3
import sys

if len(sys.argv) <= 1:
    print(f'none')
else :
    for i in range(1,len(sys.argv)):
        print(f'{sys.argv[i].upper()}')