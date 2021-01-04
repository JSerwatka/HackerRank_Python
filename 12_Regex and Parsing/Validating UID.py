import re

pattern = re.compile(r"^(?=(?:.*[A-Z]){2,})(?=(?:.*[0-9]){3,}){3,}(?:([a-zA-Z0-9])(?!.*\1)){10}$")

for _ in range(int(input())):
    if re.fullmatch(pattern, input()):
        print("Valid")
    else:
        print("Invalid")