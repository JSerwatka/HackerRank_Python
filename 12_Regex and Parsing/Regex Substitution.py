import re

def replace_str(match):
    if match.group(0) == "&&":
        return "and"
    else:
        return "or"

for _ in range(int(input())):
    print(re.sub("(?<=\s)(&&|\|\|)(?=\s)", replace_str, input()))