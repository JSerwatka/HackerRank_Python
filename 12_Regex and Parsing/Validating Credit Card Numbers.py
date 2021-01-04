import re

pattern = re.compile(r"^"
                     r"(?:4|5|6)(?:(?:(\d)(?!\1{3}|\1{2}\-\1|\1\-\1{2}|\-\1{3})){3}\-?)"
                     r"(?:(?:(\d)(?!\2{3}|\2{2}\-\2|\2\-\2{2}|\-\2{3})){4}\-?){2}"
                     r"(?:(\d)(?!\3{3})){4}"
                     r"$")

for _ in range(int(input())):
    if re.fullmatch(pattern, input()):
        print("Valid")
    else:
        print("Invalid")