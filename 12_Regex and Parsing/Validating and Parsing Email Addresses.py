# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, email.utils

pattern = r"^([A-Za-z])([\w\.-]+)@([A-Za-z]+)\.([A-Za-z]{1,3})$"

for _ in range(int(input())):
    current_email = email.utils.parseaddr(input())
    if re.match(pattern, current_email[1]):
        print(email.utils.formataddr(current_email))
