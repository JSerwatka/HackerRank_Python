def swap_case(s):
    reversed_string = ""

    for letter in s:
        if letter.isupper():
            reversed_string += letter.lower()
        elif letter.islower():
            reversed_string += letter.upper()
        else:
            reversed_string += letter

    return reversed_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)