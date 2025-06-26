#!/usr/bin/env python3

def average(classroom):
    studen_n = len(classroom)
    score = 0
    for key , value in classroom.items():
        score += value
    mean_score = score / studen_n
    return mean_score

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")