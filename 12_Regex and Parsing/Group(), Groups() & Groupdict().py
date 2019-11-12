# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

m = re.search(r"([a-zA-Z0-9])\1+", input())

if not m:
    print("-1")
else:
    print(m.group(1))
