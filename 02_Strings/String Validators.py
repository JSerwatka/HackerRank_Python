if __name__ == '__main__':
    s = input()
    is_alnum = False
    is_alpha = False
    is_digit = False
    is_lower = False
    is_upper = False
    
    for letter in s:
        if letter.isupper():
            is_alnum = True
            is_alpha = True
            is_upper = True
        elif letter.islower():
            is_alnum = True
            is_alpha = True
            is_lower = True
        elif letter.isdigit():
            is_alnum = True
            is_digit = True
    
    print(is_alnum, is_alpha, is_digit, is_lower, is_upper, sep='\n')