import math
import os
import random
import re
import sys

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())

if N % 2 == 1:
    print("Weird")
else:
    if N > 1 and N <= 5:
        print("Not Weird")
    elif N > 5 and N <= 20:
        print("Weird")
    elif N > 20 and N <= 100:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
