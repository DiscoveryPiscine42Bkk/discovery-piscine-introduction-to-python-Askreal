#!/usr/bin/env python3
import sys
import re

if len(sys.argv) <= 1:
    print('none')
else:
    for i in range(1, len(sys.argv)):
        word = sys.argv[i]
        if not re.search('ism$', word):
            print(f'{word}ism')
