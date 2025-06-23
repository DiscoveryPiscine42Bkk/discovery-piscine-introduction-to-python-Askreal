#! /usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [x + 2 for x in original_array]
greater_array = [i for i in new_array if i > 5]

print(original_array)
print(greater_array)
