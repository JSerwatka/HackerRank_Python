#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name_list = s.split(" ")
    output_string = ""

    for i in range(len(name_list)):
        if name_list[i] != "":
            name_list[i] = name_list[i][0].upper() + name_list[i][1:]
            output_string += name_list[i] + " "
        else:
            output_string += " "

    return output_string[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
