# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r"[7-9]\d{9}$"

for _ in range(int(input())):
    if re.match(pattern, input()):
        print("YES")
    else:
        print("NO")
