#!/usr/bin/env python3
import re
import sys

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    txt = sys.argv[2]
    time_key = len(re.findall(keyword , txt))
    print(time_key)
else :
    print(f'none')