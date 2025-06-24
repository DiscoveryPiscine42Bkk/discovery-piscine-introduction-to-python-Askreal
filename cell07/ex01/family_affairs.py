#!/usr/bin/env python3

def find_the_redheads(mem):
    red_haired = []
    red_haired = [key for key, value in mem.items() if value == 'red']
    return red_haired

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))
