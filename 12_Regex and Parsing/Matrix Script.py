import math
import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
new_string = ""

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for j in range(m):
    for i in range(n):
        new_string += matrix[i][j]

print(re.sub(r"(?<=[a-zA-Z0-9])\W+(?=[a-zA-Z0-9])", " ", new_string))