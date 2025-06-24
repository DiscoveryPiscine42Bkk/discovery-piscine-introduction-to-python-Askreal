#!/usr/bin/env python3
import sys
if len(sys.argv) !=3:
    print(f'none')
else :
    num_1 = int(sys.argv[1])
    num_2 = int(sys.argv[2])
    ans = [x for x in range (num_1 , num_2+1)]
    print(ans)