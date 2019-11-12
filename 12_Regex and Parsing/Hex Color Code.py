import re

N = int(input())
pattern = r"#[0-9A-F]{3,6}(?=\S)"

for _ in range(N):
    colors_found = re.findall(pattern, input(), re.I)
    if colors_found:
        print(*colors_found, sep="\n")
