import re


''' moje
thousands = "M{0,3}"
hundreds = "(C[MD]]|D?C{0,3})"
tens = "(X[CL]|L?X{0,3})"
ones = "(I[XV]|V?I{0,3})"
'''

# ulepszone
thousands = "M{0,3}"
hundreds = "(CM|D?C{0,3}|CD)"
tens = "(XC|L?X{0,3}|XL)"
ones = "(IX|V?I{0,3}|IV)"

regex_pattern = r"^%s?%s?%s?%s?$" % (thousands, hundreds, tens, ones) # Do not delete 'r'.

print(str(bool(re.match(regex_pattern, input()))))
