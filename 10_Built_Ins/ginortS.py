# można też użyć właściwości ASCII liczb
string_to_sort = input()
lower_case_letters = ""
upper_case_letters = ""
odd_numbers = ""
even_numbers = ""

for letter in string_to_sort:  
    if letter.islower():
        lower_case_letters += letter
    elif letter.isupper():
        upper_case_letters += letter
    elif letter.isdigit() and int(letter)%2 == 1:
        odd_numbers += letter
    elif letter.isdigit() and int(letter)%2 == 0:
        even_numbers += letter

print("".join(sorted(lower_case_letters) + sorted(upper_case_letters) + sorted(odd_numbers) + sorted(even_numbers)), end='')

'''my first solution
import re

string_to_sort = input()
lower_case_pattern = r"[a-z]"
upper_case_pattern = r"[A-Z]"
odd_numbers_pattern = r"[13579]"
even_numbers_pattern = r"[02468]"

lower_case_letters = ""
upper_case_letters = ""
odd_numbers = ""
even_numbers = ""

for letter in string_to_sort:  
    if re.match(lower_case_pattern, letter):
        lower_case_letters += letter
    elif re.match(upper_case_pattern, letter):
        upper_case_letters += letter
    elif re.match(odd_numbers_pattern, letter):
        odd_numbers += letter
    elif re.match(even_numbers_pattern, letter):
        even_numbers += letter

print("".join(sorted(lower_case_letters) + sorted(upper_case_letters) + sorted(odd_numbers) + sorted(even_numbers)), end='')'''
