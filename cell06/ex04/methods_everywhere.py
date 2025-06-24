#!/usr/bin/env python3
import sys 

def shrink(txt):
    a = slice(0,8)
    return(txt[a])

def enlarge(txt):
    n = 8 - len(txt)
    txt += 'Z' *n
    return txt

if len(sys.argv) <= 1:
    print(f'none')
else :
    for word in sys.argv[1:]:
        if len(word) == 8:
            print(f'{word}')
        elif len(word) < 8:
            print(enlarge(word))
        else :
            print(shrink(word))