def count_substring(string, sub_string):
    count = 0
    
    while string.find(sub_string) > -1:
        string = string[:string.find(sub_string)] + string[string.find(sub_string) + len(sub_string) - 1:]
        count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)