vowels = "AEIOU"

def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif stuart_score < kevin_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

# not optimal
# def minion_game(string):
#     stuart = []
#     kevin = []
    
#     for idx, letter in enumerate(string):
#         for i in range(len(string[idx:])):
#             if i == 0:
#                 my_slice = slice(idx, None)
#             else:
#                 my_slice = slice(idx, -1*i) 
#             if letter in vowels:
#                 kevin.append(string[my_slice])
#             else:
#                 stuart.append(string[my_slice])

#     if len(stuart) > len(kevin):
#         print(f"Stuart {len(stuart)}")
#     elif stuart_score < kevin_score:
#         print(f"Kevin {kevin_score}")
#     else:
#         print("Draw")
if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)
