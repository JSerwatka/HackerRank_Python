import re

string, pattern = input(), input()
current_char = 0
start_end_list = []

while(True):
    m = re.search(pattern, string[current_char:])
    if re.search(pattern, string[current_char:]):
        start_end_list.append((m.start()+current_char, m.end()+current_char-1))
        if m.end() - m.start() == 1:
            current_char = current_char + m.end()
        else:
            current_char = current_char + m.end() - 1
        
    else:
        if not start_end_list:
            print("(-1, -1)")
        else:
            print(*start_end_list, sep="\n")
        break
