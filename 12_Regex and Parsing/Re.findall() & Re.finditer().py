# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

string = input()
vowels = "AEIOU" 
consonants = "QWRTYPSDFGHJKLZXCVBNM"

subsets = re.findall(r"(?<=[%s])[%s]{2,}(?=[%s])" % (consonants, vowels, consonants), string, re.I)

if not subsets:
    print("-1")
else:
    print(*subsets, sep='\n')
    