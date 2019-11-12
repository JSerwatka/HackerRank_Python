# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

#We do not need ^ in the beginning because re.match() only matches from start.
pattern = r"[+-]?\d*\.\d+$"

for _ in range(int(input())):
    a = input()

    if re.match(pattern, a):
        print(True)
    else:
        print(False)
